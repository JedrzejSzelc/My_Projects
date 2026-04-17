#!/bin/bash

#######################################################################
### Title:          	ImageMagick - images batch processing		###
### Subtitle:			Rotate and crop .jpg images in batch		###
### Bash command:		image_batch_rotate_crop						###
### Version:        	20260417                               		###
### Creator:        	Jedrzej (Andrew) Szelc                 		###
### Maintainer:     	Jedrzej (Andrew) Szelc                 		###
### GitHub: 			https://github.com/JedrzejSzelc 			###
### Comments:       	works with .jpg files only.					###
###						You can modify image crop settings			###
###						or rotate angle.							###
#######################################################################

####################
### Help Section ###
####################

if [ "$1" == "-h" ] || [ "$1" == "--help" ] ; then

	printf "Usage: image_batch_rotate_crop [OPTIONAL ARGUMENTS]\n"
	printf "Crops and rotates all .jpg images available within the current directory.\n"
	printf "\n"
	printf "Optional input arguments (to be provided without the \"-\" sign):\n"
	printf "\t1st argument - rotate output image right by degrees given. (default: 0)\n"
	printf "\t2nd argument - output image width in pixels (default: 1625)\n"
	printf "\t3rd argument - output image height in pixels (default: 2310)\n"
	printf "\t4th argument - crop starting point in pixels from left edge (default: 15)\n"
	printf "\t5th argument - crop starting point in pixels from top edge (default: 15)\n"
	printf "\n"
	printf "Example:\n"
	printf "\timage_batch_rotate_crop 90			- will rotate all images right by 90 degrees only.\n"
	printf "\timage_batch_rotate_crop 45 800 600 50 100	- will rotate all images right by 45 degrees.\n"
	printf "\t 						  Will crop images starting 50 pixels from left and 100 from top.\n"
	printf "\t 						  The output images will be 800 pixels wide and 600 pixels in height.\n"
	exit 0

fi

###################################
### Variables and configuration ###
###################################

### My default rotate and crop values:
integer_rotate_degree="${1:-0}"
integer_crop_output_width_pixels="${2:-1625}"
integer_crop_output_height_pixels="${3:-2310}"
integer_crop_left_edge_distance_pixels="${4:-15}"
integer_crop_top_edge_distance_pixels="${5:-15}"

##########################
### Script starts here ###
##########################

### Create output directory:
string_output_directory="processed_images"
mkdir -p "$string_output_directory"

### Batch processing of all .jpg images available within the current directory:
for current_image_file in *.jpg; do
	convert "$current_image_file" \
	-crop "$integer_crop_output_width_pixels"x"$integer_crop_output_height_pixels"+"$integer_crop_left_edge_distance_pixels"+"$integer_crop_top_edge_distance_pixels" \
	-rotate "$integer_rotate_degree" \
	"$string_output_directory"/"$current_image_file"
done
