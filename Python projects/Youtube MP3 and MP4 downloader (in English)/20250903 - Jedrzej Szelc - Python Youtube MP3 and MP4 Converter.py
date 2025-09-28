###################################################################
### Title: 2025.09.03 - Python Youtube downloader (MP3 and MP4) ###
### Author: Jędrzej (Andrew) Szelc                              ###
### Based on:                                                   ###
###     - https://pypi.org/project/pytubefix/                   ###
###     - https://github.com/juanbindez/pytubefix               ###
###################################################################

#######################
### General modules ###
#######################
import os
from pathlib import Path

#############
### Setup ###
#############
string_mp3_download_directory_name = "Downloads_MP3"
Path(string_mp3_download_directory_name).mkdir(parents=True, exist_ok=True)
string_mp4_download_directory_name = "Downloads_MP4"
Path(string_mp4_download_directory_name).mkdir(parents=True, exist_ok=True)

############################################
### Audio - Download MP3 - A single song ###
############################################

# # Single song url
# string_url_single_song_only = 'https://www.youtube.com/watch?v=uK51flc3eM8'
#
# # Song download begins
# from pytubefix import YouTube
# from pytubefix.cli import on_progress
# yt = YouTube(string_url_single_song_only, on_progress_callback=on_progress)
# ys = yt.streams.get_audio_only()
# ys.download(output_path=string_mp3_download_directory_name)

##################################################
### Audio - Download MP3 - A complete playlist ###
##################################################

# # Playlist URL and name (download folder name)
# string_playlist_url = "https://www.youtube.com/watch?v=ZyhVh-qRZPA&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS"
# string_playlist_name = "Pandas tutorials"
#
# # Make directories for download
# string_complete_download_directory = string_mp3_download_directory_name + "/" + string_playlist_name
# Path(string_complete_download_directory).mkdir(parents=True, exist_ok=True)
#
# # Playlist download begins
# from pytubefix import Playlist
# from pytubefix.cli import on_progress
# pl = Playlist(string_playlist_url)
# for video in pl.videos:
#     ys = video.streams.get_audio_only()
#     ys.download(output_path=string_complete_download_directory)

##################################################
### Video - Download MP4 - A complete playlist ###
##################################################

# # Playlist URL and name (download folder name)
# string_playlist_url = "https://www.youtube.com/watch?v=ZyhVh-qRZPA&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS"
# string_playlist_name = "Pandas tutorials"
#
# # Make directories for download
# string_complete_download_directory = string_mp4_download_directory_name + "/" + string_playlist_name
# Path(string_complete_download_directory).mkdir(parents=True, exist_ok=True)
#
# # Playlist download begins
# from pytubefix import Playlist
# from pytubefix.cli import on_progress
# pl = Playlist(string_playlist_url)
# for video in pl.videos:
#     print("MP4 DOWNLOAD WARNING: Low resolution only. Sorry...")
#     ys = video.streams.get_highest_resolution()
#     ys.download(output_path=string_complete_download_directory)

#################################################
### Audio - Download MP3 - A complete channel ###
#################################################

# # Channel URL and name (download folder name)
# string_channel_url = "https://www.youtube.com/c/Coreyms/playlists"
# string_channel_name = "Complete Channel - Schafer"
#
# # Make directories for download
# string_complete_download_directory = string_mp3_download_directory_name + "/" + string_channel_name
# Path(string_complete_download_directory).mkdir(parents=True, exist_ok=True)
#
# # Channel download begins
# from pytubefix import Channel
# c = Channel(string_channel_url)
# for video in c.videos:
#     ys = video.streams.get_audio_only()
#     ys.download(output_path=string_complete_download_directory)

#################################################
### Video - Download MP4 - A complete channel ###
#################################################

# Channel URL and name (download folder name)
string_channel_url = "https://www.youtube.com/c/Coreyms/playlists"
string_channel_name = "Complete Channel - Schafer"

# Make directories for download
string_complete_download_directory = string_mp4_download_directory_name + "/" + string_channel_name
Path(string_complete_download_directory).mkdir(parents=True, exist_ok=True)

# Channel download begins
from pytubefix import Channel
c = Channel(string_channel_url)
for video in c.videos:
    print("MP4 DOWNLOAD WARNING: Low resolution only. Sorry...")
    ys = video.streams.get_highest_resolution()
    ys.download(output_path=string_complete_download_directory)