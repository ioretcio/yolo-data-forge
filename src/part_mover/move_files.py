import os
import shutil
import argparse


def move_files():
    parser = argparse.ArgumentParser(
        description='Moves only specific part of data to another folder(sorted by name). Can be helpful in pack creation.')

    parser.add_argument('--source', "-s", help="source directory")
    parser.add_argument('--destination', "-d", help="destination directory")
    parser.add_argument('--number', "-n", help="Number of files to move")
    args = parser.parse_args()
    source_path = args.source
    dest_path = args.destination
    number = args.number
    
    files_to_move = os.listdir(source_path)
    files_to_move = sorted(files_to_move)[:number]

    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    
    
    for file in files_to_move:
        file_path = os.path.join(source_path, file)
        shutil.move(file_path, dest_path)
