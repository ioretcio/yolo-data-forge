import argparse
import cv2
import os
import numpy as np

def sort():
    parser = argparse.ArgumentParser(
        description='This sorts(renames with numbers) images by its brightness and returns afterwork.')
    parser.add_argument('--root_dir', "-d", help="Root directory of deleting")
    
    args = parser.parse_args()
    directory_path = args.root_dir

    average_laplacians = {}
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                image_path = os.path.join(root, file)
                
                image = cv2.imread(image_path)
                if np.any(image):  
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    laplacian = cv2.Laplacian(gray, cv2.CV_64F).var()
                    average_laplacians[file] = laplacian
                else:
                    print("Unable to load image at path {}".format(image_path))
                    
    sorted_image_info = dict(sorted(average_laplacians.items(), key=lambda item: item[1]))
    newnames = {}
    counter = 0
    for key in sorted_image_info.keys():
        counter+=1
        newnames[key] = f"{   str(counter).zfill(10) }.{key.split('.')[-1]}"
    for old_name, new_name in newnames.items():
        if os.path.exists(os.path.join(directory_path, old_name)):
            os.rename(os.path.join(directory_path, old_name), os.path.join(directory_path, new_name))
    input("Press any key to perform reverse renaming:")
    for old_name, new_name in newnames.items():
        if os.path.exists(os.path.join(directory_path, new_name)):
            os.rename(os.path.join(directory_path, new_name), os.path.join(directory_path, old_name))
