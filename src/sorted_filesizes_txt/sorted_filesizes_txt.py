import os
import argparse

def sorted_filesizes_txt():
    parser = argparse.ArgumentParser(description='Creates filesizes.txt files whis includes \
        sorted by size list of files, recursively found in dir.')
    parser.add_argument( '--source_folder', '-s', type=str, help='path to the source folder')
    args = parser.parse_args()
    source_folder = args.source_folder
    source_folder_name = os.path.basename(os.path.normpath(source_folder))
    file_sizes = {}
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.relpath(os.path.join(root, file), start=source_folder)
            file_sizes[file_path] = os.path.getsize(os.path.join(source_folder, file_path))
    
    file_sizes = dict(sorted(file_sizes.items(), key=lambda item: item[1], reverse=True))


    with open(f'{source_folder_name}_file_sizes.txt', 'w') as file:
        for key, value in file_sizes.items():
            file.write(f"{key}: {value}\n")

sorted_filesizes_txt()