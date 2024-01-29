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

def exact_cleaner():
    parser = argparse.ArgumentParser(
        description='This program compares images pixel by pixel and deletes duplicate images based on their file sizes and pixel diff.')
    parser.add_argument('--dump_file', "-f", help="file with list of dirs and sizes")
    parser.add_argument('--root_dir', "-d", help="Root directory of deleting")
    
    args = parser.parse_args()

    file_path = args.dump_file
    directory_path = args.root_dir
    
    
    data = []    
    with open(file_path, 'r',encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            parts = line.split(':')
            if not parts[0].strip().lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                continue
            data.append([ os.path.join(directory_path,parts[0].strip()), parts[1].strip()])

    for i in range(len(data)-1):
        if data[i][1] == data[i+1][1]:
            similarity = compare_images_pixel_by_pixel(cv2.imread(data[i][0]),  cv2.imread(data[i+1][0]), data[i][0])
            if similarity:
                print(f"deleting {data[i][0] } bacause {data[i+1][0]} looks same")
                os.remove(data[i][0])
                del data[i]
exact_cleaner()