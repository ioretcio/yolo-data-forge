import os
import argparse


def add_extension():
    parser = argparse.ArgumentParser(
        description='This program add extension to broken files')
    parser.add_argument("--folder_path", help="Path to the folder", type=str)
    parser.add_argument("--extension", help="File extension to add (with a point)", type=str)
    args = parser.parse_args()
    folder_path = args.folder_path
    extension = args.extension
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) > 200000:
                if not file_path.endswith(extension):
                    new_file_path = file_path + extension
                    os.rename(file_path, new_file_path)
