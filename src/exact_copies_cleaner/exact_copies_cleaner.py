import os
import cv2
import numpy as np
import argparse

def compare_images_pixel_by_pixel(image1, image2, impath):
    try:
        if image1.shape != image2.shape:
            return False
    except Exception as e:
        if  'has no attribute' in str(e):
            print(impath)
            exit()
    difference = cv2.subtract(image1, image2)
    b, g, r = cv2.split(difference)
    return not np.any(b) and not np.any(g) and not np.any(r)

def sorted_filesizes(source_folder):
    file_sizes = {}
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.relpath(os.path.join(root, file), start=source_folder)
            file_sizes[file_path] = os.path.getsize(os.path.join(source_folder, file_path))
    
    file_sizes = dict(sorted(file_sizes.items(), key=lambda item: item[1], reverse=True))
    result = []
    for key, value in file_sizes.items():
        result.append([key, value])
    print(f"Finished creation of filelist, appended {len(result)} candidats")
    return result

def exact_cleaner():
    parser = argparse.ArgumentParser(
        description='This program compares images pixel by pixel and deletes duplicate images based on their file sizes and pixel diff.')
    parser.add_argument('--root_dir', "-d", help="Root directory of deleting")
    args = parser.parse_args()
    directory_path = args.root_dir
    data = sorted_filesizes(directory_path)
    count = 0
    for i in range(len(data)-1):
        if data[i][1] == data[i+1][1]:
            similarity = compare_images_pixel_by_pixel(\
                cv2.imread( os.path.join( directory_path, data[i][0]) ),\
                cv2.imread(os.path.join( directory_path,data[i+1][0])), data[i][0] )
            if similarity:
                print(f"deleting { os.path.join( directory_path, data[i][0]) } bacause { os.path.join( directory_path, data[i+1][0])} looks same")
                os.remove(os.path.join( directory_path, data[i][0]))
                del data[i]
                count +=1
                
    print(f"{count} files was deleted")
exact_cleaner()