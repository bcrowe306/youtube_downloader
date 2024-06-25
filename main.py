#!python3

from pytube import YouTube 
import sys
import os
from pathlib import Path



# where to save 
def progressBar(stream, chuck, bytesRemaining):
    os.system('clear')
    percentage = round( (stream.filesize - bytesRemaining) / stream.filesize, 2)*100
    t: str = stream.title
    print(f"{t}: {percentage}% complete")

# Get link from command line args
link = sys.argv[1]
# object creation using YouTube 
yt = YouTube(link, on_progress_callback=progressBar) 

# Get all streams and filter for mp4 files
mp4_streams: list = yt.streams.filter(file_extension='mp4')
# get the video with the highest resolution
d_video = mp4_streams[-1]
title: str = yt.vid_info["videoDetails"]["title"]
title = title.replace(",", "")

for i, stream in enumerate(mp4_streams):
    print(f"{i}: {stream.resolution}")

index = input("Select a resolution: ")
d_video=mp4_streams[int(index)]

# Configure path
homePath = os.environ['HOME']
SAVE_PATH = "/home/chintusharma/Downloads" #to_do 
filePath = Path(f"{homePath}/downloads/{title}.mp4")


# Delete file if exists;
if filePath.exists():
    os.remove(filePath)

try: 
    # downloading the video 
    print(f"Downloading video to: {filePath}")
    d_video.download(output_path=str(filePath))
except: 
    print("Some Error!")