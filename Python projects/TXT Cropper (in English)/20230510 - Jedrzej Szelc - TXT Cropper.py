###################################################################################################
### Title:          TXT-Cropper                                                                 ###
### Version:        20230510                                                                    ###
### Creator:        jedrzej.szelc@capgemini.com                                                 ###
### Maintainer:     jedrzej.szelc@capgemini.com                                                 ###
### Comments:       This script is used for selectively removing characters from a .txt file.   ###
###################################################################################################

######################
### Python Modules ###
######################

import os
import string
import shutil

#########################
### General Functions ###
#########################

def Remove_Dir(string_Dir_Name):
   shutil.rmtree(string_Dir_Name)

def Function_Dir_Setup(string_Dir_Name):
       os.makedirs(string_Dir_Name, exist_ok=True)

def function_Import_TXT_File_and_Return_It_As_2D_List(string_Input_TXT_Filename_with_extension_with_file_path):
    with open(string_Input_TXT_Filename_with_extension_with_file_path, "r") as handler_txt_read_complete_input_file:
        list_TXT_File_Content = handler_txt_read_complete_input_file.readlines()
        handler_txt_read_complete_input_file.close()
    return list_TXT_File_Content

def function_Save_TXT_File(string_Input_TXT_Filename_with_extension_with_file_path, list_TXT_File_Content):
    with open(string_Input_TXT_Filename_with_extension_with_file_path, "a") as handler_txt_read_complete_output_file:
        for integer_TXT_Lines_Counter in range(len(list_TXT_File_Content)):
            handler_txt_read_complete_output_file.write(list_TXT_File_Content[integer_TXT_Lines_Counter])
        handler_txt_read_complete_output_file.close()

######################################
### The proper program starts here ###
######################################

### Input files - you may modify this part of code.
string_TXT_Filename_with_extension = "IABV.2023-05-04T0051.txt"

### Fields to be modified - you may modify this part of code, but BE CAREFUL!
list_Indices_to_be_removed = \
    [
        [262, 262],
        [221, 236],
        [186, 186],
        [185, 185],
        [109, 110],
        [50, 51]
    ]

### General settings - do not modify this part of code.
string_Output_Dir_Name = "Output TXT File"
string_Input_TXT_Filename_with_extension_with_file_path = "Input TXT File/" + string_TXT_Filename_with_extension
string_Output_TXT_Filename_with_extension_with_file_path = string_Output_Dir_Name + "/Processed-" + string_TXT_Filename_with_extension

### Refresh Output Dir - do not modify this part of code.
Function_Dir_Setup(string_Output_Dir_Name)
Remove_Dir(string_Output_Dir_Name)
Function_Dir_Setup(string_Output_Dir_Name)

### Import the TXT file - do not modify this part of code.
list_File_After_Import = function_Import_TXT_File_and_Return_It_As_2D_List(string_Input_TXT_Filename_with_extension_with_file_path)

### Process the TXT file content - do not modify this part of code.
for integer_indices_counter in range(len(list_Indices_to_be_removed)):
    list_current_indices = list_Indices_to_be_removed[integer_indices_counter]
    list_current_indices[0] = list_current_indices[0]-1

sorted(list_Indices_to_be_removed, key=lambda x: x[1], reverse=True)

for integer_TXT_Lines_Counter in range(len(list_File_After_Import)):
    current_line_to_be_modified = list_File_After_Import[integer_TXT_Lines_Counter]
    current_modified_line = current_line_to_be_modified
    for integer_indices_counter in range(len(list_Indices_to_be_removed)):
        list_current_indices = list_Indices_to_be_removed[integer_indices_counter]
        integer_current_Start_Index = list_current_indices[0]
        integer_current_Finish_Index = list_current_indices[1]
        for integer_index_removal_counter in range(integer_current_Finish_Index, integer_current_Start_Index, -1):
            current_line_to_be_modified = current_line_to_be_modified[:integer_index_removal_counter-1]+current_line_to_be_modified[integer_index_removal_counter:]
    list_File_After_Import[integer_TXT_Lines_Counter] = current_line_to_be_modified

### Save the processed TXT file - do not modify this part of code.
function_Save_TXT_File(string_Output_TXT_Filename_with_extension_with_file_path, list_File_After_Import)