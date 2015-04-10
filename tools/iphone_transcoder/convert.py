import os
import sys
import shutil
# import subprocess

# input
filename = sys.argv[1]

# vars
output_folder = "output2"
audio_file_name = output_folder + "/audio.mp3"
image_file_name = output_folder + "/image_%05d.jpg"

# create folder
if os.path.exists(output_folder):
	shutil.rmtree(output_folder)
os.makedirs(output_folder)

# extract audio
print "=== Converting Audio ==="
command = "ffmpeg -i {0} -b:a 192k -map a {1}".format(filename, audio_file_name) 
os.system(command)

print "=== Converting Images ==="
command = "ffmpeg -i {0} -r 25 -vf scale=640:-1 -q:v 9 -an -f image2 {1}".format(filename, image_file_name) 
os.system(command)
