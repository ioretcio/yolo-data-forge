import shutil
import random
import os
from os import listdir, mkdir, makedirs
from os.path import isfile, join, isdir
import argparse


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


def train_val_split():
    parser = argparse.ArgumentParser(
        description='Splits images and annotations in a selected percentage configuration across training, validation, and test folders')

    parser.add_argument('--source_images', "-i", type=dir_path, help="source images directory")
    parser.add_argument('--source_labels', "-l", type=dir_path, help="source labels directory")

    parser.add_argument('--result', "-r", type=dir_path, help="result images-labels directory")
    parser.add_argument('--train_percent', "--train", "-t", type=int, help="percent of data to train set")

    parser.add_argument('--validation_percent', "--val", "-v", type=int, help="percent of data to validation set")

    args = parser.parse_args()

    train_percent = int(args.train_percent)
    validation_percent = int(args.validation_percent)

    source_images_path = args.source_images
    source_labels_path = args.source_labels
    result_path = args.result

    test_percent = 100 - (train_percent + validation_percent)
    files = []

    img_files = [f for f in listdir(source_images_path) if isfile(join(source_images_path, f))]
    label_files = [f.replace(".png", ".txt").replace(".JPG", ".txt").replace(".jpg", ".txt").replace(".jpeg", ".txt")
                   for f in img_files]

    for i in range(len(img_files)):
        files.append([source_images_path, img_files[i], source_labels_path, label_files[i]])

    random.shuffle(files)

    train_count = int(len(files) * train_percent / 100)
    valid_count = int(len(files) * validation_percent / 100)
    test_count = int(len(files) * test_percent / 100)

    if isdir(result_path):
        shutil.rmtree(result_path)

    mkdir(result_path)

    makedirs(result_path + "/train/images")
    makedirs(result_path + "/train/labels")

    for i in range(0, train_count):
        print(f"Train {(i / train_count) * 100}%")
        shutil.copyfile(files[i][0] + files[i][1], result_path + "/train/images/" + files[i][1])
        shutil.copyfile(files[i][2] + files[i][3], result_path + "/train/labels/" + files[i][3])

    makedirs(result_path + "/val/images")
    makedirs(result_path + "/val/labels")

    for i in range(0, valid_count):
        print(f"Valid {(i / valid_count) * 100}%")
        shutil.copyfile(files[i][0] + files[i][1], result_path + "/val/images/" + files[i][1])
        shutil.copyfile(files[i][2] + files[i][3], result_path + "/val/labels/" + files[i][3])

    if test_count > 0:
        makedirs(result_path + "/test/images")
        makedirs(result_path + "/test/labels")

        for i in range(0, test_count):
            print(f"Test {(i / test_count) * 100}%")
            shutil.copyfile(files[i][0] + files[i][1], result_path + "/test/images/" + files[i][1])
            shutil.copyfile(files[i][2] + files[i][3], result_path + "/test/labels/" + files[i][3])
