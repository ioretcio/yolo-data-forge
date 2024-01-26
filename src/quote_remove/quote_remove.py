import os
import argparse

def remove_in_dir():
    parser = argparse.ArgumentParser(
        description='Renames all files in the specified directory, removing quotes from the filenames')

    parser.add_argument('--directory', '-d', type=str, help='path to the directory containing files to be renamed, removing quotes from the filenames')
    args = parser.parse_args()

    directory = int(args.directory)
    for root, dirs, files in os.walk(directory):
        for file in files:
            count+=1
            if "'" in file:
                new_name = file.replace("'", "")
                if not os.path.exists(os.path.join(root, new_name)):
                    os.rename(os.path.join(root, file), os.path.join(root, new_name))
                else:
                    user_input = input(f"Do you want to delete the [{os.path.join(root, file)}] file? (y/n): ")
                    if user_input.lower() == 'y':
                        os.remove(os.path.join(root, file))
    print(count)
