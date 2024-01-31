import os
import shutil
import random
import string
import argparse

def merge():
    parser = argparse.ArgumentParser(
        description='Carefully move files from one folder to other and add random symbols in case of conflicts.')
    parser.add_argument("--source", "-s" , help="Path to the folder", type=str)
    parser.add_argument("--destination",'-d', help="File extension to add", type=str)
    args = parser.parse_args()
    source_folder = args.source_folder
    destination_folder = args.destination_folder
    
    
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # if file.lower().endswith(".mp4"):
            source_path = os.path.join(root, file)
            
            destination_path = os.path.join(destination_folder, file)
            if not os.path.exists(destination_path):
                shutil.move(source_path, destination_path)
            else:
                if os.path.getsize(destination_path) == os.path.getsize(source_path):
                    os.remove(source_path)
                else:
                    print(f"Different sizes {destination_path} and {source_path} ... {os.path.getsize(destination_path)} {os.path.getsize(source_path)}")
                    new_file_name = os.path.splitext(source_path)[0] +random.choice(string.ascii_lowercase) + os.path.splitext(source_path)[1]
                    os.rename(source_path, new_file_name)