#!/bin/bash

#######################################################################
### Title:              ImageMagick - images batch processing       ###
### Subtitle:           Compress .jpg images in batch               ###
### Bash command:       image_batch_compress                        ###
### Version:            20260427                                    ###
### Creator:            Jedrzej (Andrew) Szelc                      ###
### Maintainer:         Jedrzej (Andrew) Szelc                      ###
### GitHub:             https://github.com/JedrzejSzelc             ###
### Comments:           works with .jpg files only.                 ###
###                     You can modify the compression level.       ###
#######################################################################

####################
### Help Section ###
####################

if [ "$1" == "-h" ] || [ "$1" == "--help" ] ; then

	printf "Usage: image_batch_compress [OPTIONAL COMPRESSION LEVEL]\n"
    printf "Compresses all .jpg images available within the current directory.\n"
    printf "\n"
    printf "Optional argument (to be provided without the \"-\" sign) is the .jpg compression level in percent (default value is 25 percent).\n"
    printf "\n"
    printf "Example:\n"
    printf "\timage_batch_compress		- will compress all images with a default 25%% compression rate.\n"
    printf "\timage_batch_compress 50		- will compress all images with a 50%% compression rate.\n"
    exit 0

fi

###################################
### Variables and configuration ###
###################################

### My default rotate and crop values:
integer_compression_factor_percent="${1:-25}"
integer_quality_factor_percent=$((100-integer_compression_factor_percent))

##########################
### Script starts here ###
##########################

### Create output directory:
string_output_directory="processed_images"_"$integer_compression_factor_percent"
mkdir -p "$string_output_directory"

### Batach processing of all .jpg images available within the current directory:
for current_image_file in *.jpg; do
	convert "$current_image_file" \
	-quality "$integer_quality_factor_percent"% \
	"$string_output_directory"/"$current_image_file"
done