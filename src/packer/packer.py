import argparse
import os
import shutil
import random


def dir_path(string):
    if os.path.isdir(string): return string
    else: raise NotADirectoryError(string)

extensions = ['jpg', 'png', 'JPG']

def ends(file):
    for extension in extensions:
        if(file.endswith(extension)):
            return True
    return False

def main(images_folder,labels_folder, packs_count, packs_name):
    siz = int(len(os.listdir(images_folder))/packs_count)
    print(f"I going to create {siz} packs")
    for i in range(1, packs_count + 1):
        pack_folder = f'{packs_name}{i:04d}'
        images_folder = os.path.join(pack_folder, 'images')
        labels_folder = os.path.join(pack_folder, 'labels')
        if not os.path.exists(pack_folder):
            os.makedirs(pack_folder)
        if not os.path.exists(images_folder):
            os.makedirs(images_folder)
        if not os.path.exists(labels_folder):
            os.makedirs(labels_folder)

    for i in range(1, packs_count + 1):
        
        pack_folder = f'{packs_name}{i:04d}'
        print(f"Now i process {pack_folder}")
        images_folder = os.path.join(pack_folder, 'images')
        labels_folder = os.path.join(pack_folder, 'labels')
        shutil.copy("classes.txt", labels_folder)
        files = os.listdir(images_folder)
        random.shuffle(files)
        for file_name in files[:siz]:
            file_path = os.path.join(images_folder, file_name)
            destination_path = os.path.join(images_folder, file_name)
            if not os.path.exists(destination_path):
                shutil.move(file_path, destination_path)
                label_file_name = os.path.splitext(file_name)[0] + '.txt'
                label_file_path = os.path.join(labels_folder, label_file_name)
                if os.path.exists(label_file_path):
                    destination_label_path = os.path.join(labels_folder, label_file_name)
                    shutil.move(label_file_path, destination_label_path)
            

def packer():
    parser = argparse.ArgumentParser( description='Can split big folders into npacs' )
    parser.add_argument('--imput', "-i", type=dir_path, help="source directory images")
    parser.add_argument('--ilput', "-l", type=dir_path, help="source directory labels")
    parser.add_argument('--count', "-c", type=int, help="count of resulting packs")
    parser.add_argument('--out', "-o", type=str, help="base packs name")
    args = parser.parse_args()
    images_folder = args.imput
    labels_folder = args.ilput
    packs_count = int(args.count)
    packs_name = args.out
    main(images_folder, labels_folder, packs_count, packs_name)
