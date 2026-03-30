#!/bin/bash

#######################################################################
### Title:          	Automated rsync backup for Linux Ubuntu		###
### Bash command:		rsync_backup								###
### Version:        	20260330                               		###
### Creator:        	Jedrzej (Andrew) Szelc                 		###
### Maintainer:     	Jedrzej (Andrew) Szelc                 		###
### GitHub: 			https://github.com/JedrzejSzelc 			###
### Comments:       	Bash script for Linux Ubuntu.				###
###						Allows automated rsync backups 				###
###						also with file revisions 					###
###						(meaning: multiple, sequential copies).		###
###						Provided only as a concept - cannot 		###
###						guarantee it works out of the box.			###
#######################################################################
     
####################
### Help Section ###
####################

if [ "$1" == "-h" ] || [ "$1" == "--help" ] ; then

	printf "Usage: rsync_backup [OPTIONAL ARGUMENT]\n"
	printf "Carry out a rsync backup.\n"
	printf "\n"
	printf "Optional input arguments (to be provided without the \"-\" sign):\n"
	printf "\tq - quick back up (only some files and subfolders to be backed up)\n"
	printf "\ta - back up only the 'a' source folder (files and subfolders that belong to the 'a' source folder)\n"
	printf "\tb - back up only the 'b' source folder (files and subfolders that belong to the 'b' source folder)\n"
	printf "\n"
	printf "Example:\n"
	printf "\trsync_backup 		- will carry out a full back up.\n"
	printf "\trsync_backup q 	- will carry out a quick back up.\n"
	printf "\trsync_backup a 	- will carry out back up of the 'a' source.\n"
	exit 0

fi

###################################
### Variables and configuration ###
###################################

### File time-differentiation window:
integer_modify_window_seconds=10

### Rsync scenario selector with an input argument:
### q - quick backup. Only selected files and folders to be backed up.
if [[ "$1" == "q" ]] ; then

	string_scenario_type="\nQuick scenario"

	bool_backup_folder_only_selected_file=true
	bool_backup_folder_A=false
	bool_backup_folder_B=false

### a - back up only files and folders in the 'a' destination.
elif [[ "$1" == "a" ]]
then

	string_scenario_type="\n'A' scenario"

	bool_backup_folder_only_selected_file=false
	bool_backup_folder_A=true
	bool_backup_folder_B=false

### b - back up only files and folders in the 'b' destination.
elif [[ "$1" == "b" ]]
then

	string_scenario_type="\n'B' scenario"

	bool_backup_folder_only_selected_file=false
	bool_backup_folder_A=false
	bool_backup_folder_B=true

### Default / no argument - Full scenario. Back up all source folders.
else

	string_scenario_type="\nFull scenario"

	bool_backup_folder_only_selected_file=false
	bool_backup_folder_A=true
	bool_backup_folder_B=true

fi

#########################
### Script start time ###
#########################

printf "$string_scenario_type started "
date +"on %x at %X"

###############################
### Back up scenario: quick ###
###############################

time if [ -d "/media/destination_quick" ] && [ "$bool_backup_folder_only_selected_file" = true ] ; then

	printf "\nQuick scenario...\n"

	### Back up whatever you want:
	rsync -a --no-compress --whole-file --inplace --modify-window=$integer_modify_window_seconds --delete-before /media/source_folder/only_selected_subfolders_to_be_backed_up/ /media/destination_quick/

fi

################################################
### Back up scenario: To the 'A' destination ###
################################################

time if [ -d "/media/destination_A" ] && [ "$bool_backup_folder_A" = true ] ; then

	printf "\nTo destination 'A'...\n"

	### Back up whatever you want:
	rsync -a --no-compress --whole-file --inplace --modify-window=$integer_modify_window_seconds --delete-before /media/source_folder/folder_or_file_to_be_backed_up/ /media/destination_A/

fi

################################################
### Back up scenario: To the 'B' destination ###
################################################

time if [ -d "/media/destination_B" ] && [ "$bool_backup_folder_A" = true ] ; then

	printf "\nTo destination 'B'...\n"

	### Back up whatever you want:
	rsync -a --no-compress --whole-file --inplace --modify-window=$integer_modify_window_seconds --delete-before /media/source_folder/folder_or_file_to_be_backed_up/ /media/destination_B/

fi

#####################################
### Back up scenario: Full backup ###
#####################################

time if [ -d "/media/destination_B" ] && [ "$bool_backup_folder_A" = true ] ; then

	printf "\nFull backup...\n"

	### Back all:
	rsync -a --no-compress --whole-file --inplace --modify-window=$integer_modify_window_seconds --delete-before /media/source_folder/only_selected_subfolders_to_be_backed_up/ /media/destination_quick/
	rsync -a --no-compress --whole-file --inplace --modify-window=$integer_modify_window_seconds --delete-before /media/source_folder/folder_or_file_to_be_backed_up/ /media/destination_A/
	rsync -a --no-compress --whole-file --inplace --modify-window=$integer_modify_window_seconds --delete-before /media/source_folder/folder_or_file_to_be_backed_up/ /media/destination_B/

	### (Bonus) back up a selected file with revisions (multiple, sequential copies): 
	if [ -d /media/destination_quick/ ]; then
		mkdir -p /media/destination_quick/
	fi
	
	string_main_file_name="some_file_that_requires_back_up_with_revisions.sh"
	
	rsync -aI --delete-before /media/source_folder/$string_main_file_name /media/destination_quick/$string_main_file_name
	
	integer_number_of_revisions=20
	
	for integer_loop_iterator in $(seq 0 $(($integer_number_of_revisions-1)));
	do
		string_file_name_next=string_main_file_name"_"$((integer_number_of_revisions-$integer_loop_iterator))
		string_file_name_current=string_main_file_name"_"$((integer_number_of_revisions-$integer_loop_iterator-1))
		if [ $((integer_number_of_revisions-$integer_loop_iterator-1)) -eq 0 ]; then
			string_file_name_current=$string_main_file_name
		fi
		rsync -aI --delete-before /media/source_folder/$string_file_name_current /media/destination_quick/$string_file_name_next
	done

fi

###########################
### Finished backing up ###
###########################

printf "$string_scenario_type finished "
date +"on %x at %X"
printf "\n"