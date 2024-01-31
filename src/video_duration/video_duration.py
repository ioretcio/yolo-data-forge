import os
from moviepy.editor import VideoFileClip
import argparse


def duration():
    parser = argparse.ArgumentParser(
        description='This program counts total duration of video in folder.')
    parser.add_argument('--root_dir', "-d", help="Root directory of deleting")
    args = parser.parse_args()
    directory_path = args.root_dir
    
    total_duration = 0
    files = os.listdir(directory_path)
    filecount = len(files)
    
    current = 0
    
    
    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)
        if os.path.isfile(filepath) and any(filepath.endswith(ext) for ext in ['.mp4', '.avi', '.mkv', '.mov']):
            try:
                video = VideoFileClip(filepath)
                total_duration += video.duration
                current+=1
                print(f"duration = {total_duration}, means ~ {total_duration/(current/filecount)}, like a ~ {(total_duration/(current/filecount))/2} frames")
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    print(f"Total duration of all videos in the {directory_path}: {total_duration} seconds")