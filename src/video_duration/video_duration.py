import os
from moviepy.editor import VideoFileClip
import argparse

def duration(directory_path):
    total_duration = 0
    filecount = 0

    for root, dirs, files in os.walk(directory_path):
        filecount += len(files)
        for filename in files:
            filepath = os.path.join(root, filename)
            if any(filepath.endswith(ext) for ext in ['.mp4', '.avi', '.mkv', '.mov']):
                try:
                    video = VideoFileClip(filepath)
                    total_duration += video.duration
                    print(f"duration = {total_duration} seconds")
                except Exception as e:
                    print(f"Error processing {filename}: {e}")

    print(f"Total duration of all videos in {directory_path}: {total_duration} seconds")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This program counts the total duration of videos in a folder recursively.')
    parser.add_argument('--root_dir', "-d", help="Root directory containing videos")
    args = parser.parse_args()
    directory_path = args.root_dir
    
    if directory_path:
        duration(directory_path)
    else:
        print("Please provide the root directory using --root_dir argument.")