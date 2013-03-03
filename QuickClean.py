#Quickly clean my music, videos and images into a different directory.
import glob
import sys
import os
import shutil
import argparse


parser = argparse.ArgumentParser(description='A quick way to clean out your cluttered folders.')
parser.add_argument('-s','--source directory', help='Folder you want to clean out.', required=True)
parser.add_argument('-m','--music directory', help='Description for bar argument', required=False)
parser.add_argument('-p','--pictures directory', help='Description for bar argument', required=False)
parser.add_argument('-v','--videos directory', help='Description for bar argument', required=False)
parser.add_argument('-d','--documents directory', help='Description for bar arsgument', required=False)


#args = vars(parser.parse_args())

os.chdir("/Users/shayekharjanamit/Downloads") #source_dir
destination_dirs = ['/Users/shayekharjanamit/Music','/Users/shayekharjanamit/Videos','/Users/shayekharjanamit/Pictures','/Users/shayekharjanamit/Documents']

#Parameters to clean.
music = glob.glob("*.mp3") + glob.glob("*.flac") + glob.glob("*.aac")
pictures = glob.glob("*.png") + glob.glob ('*.jpg') + glob.glob("*.bmp")
videos = glob.glob("*.avi") + glob.glob("*.mp4") + glob.glob("*.flv")
documents = glob.glob ('*.pdf') + glob.glob ('*.PDF') + glob.glob ("*.xls") + glob.glob ("*.xlsx") + glob.glob ("*.pptx") + glob.glob ("*.docx") + glob.glob("*.m") + glob.glob("*.ppt") + glob.glob("*.doc")

   
#Copies to destination directory, and then deletes the file. This is done because shutil's copy method has the ability to overwrite. 
for songs in music:
    shutil.copy(songs,destination_dirs[0])
    os.remove(songs)
for video in videos:
    shutil.copy(video,destination_dirs[1])
    os.remove(video)
for picture in pictures:
    shutil.copy(picture,destination_dirs[2])
    os.remove(picture)
for document in documents:
    shutil.copy(document,destination_dirs[3])
    os.remove(document)

