import os
import argparse


def deleter():
    parser = argparse.ArgumentParser(
        description='Deletes all files from del_file txt list within defined root folder.')

    parser.add_argument('--directory', "-d", help="source root folder")
    parser.add_argument('--file_del', "-f", help="List file")

    args = parser.parse_args()

    root_dir = args.directory
    filedel = args.file_del
    
    file_dict = {}
    for folder, subs, files in os.walk(root_dir):
        for filename in files:
            file_dict[filename] = os.path.join(folder, filename)
    with open(filedel, 'r') as f:
        files_to_delete = [os.path.basename(line.strip()) for line in f.readlines()]

    for filetodel in files_to_delete:
        try:
            print(f"Deleting {file_dict[filetodel]}", end=' ')
            os.remove(file_dict[filetodel])
            print("ok!")
        except Exception as e:
            print(str(e))