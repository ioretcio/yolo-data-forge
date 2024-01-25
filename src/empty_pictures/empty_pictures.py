import os
import argparse


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


def empty_pictures():
    parser = argparse.ArgumentParser(
        description='Finds images and labels without a pair in the image-labels directories.')
    parser.add_argument('--images', "-i", type=dir_path, help="images directory")
    parser.add_argument('--labels', "-l", type=dir_path, help="labels directory")
    parser.add_argument('--symbol', "-s", type=str,
                        help="character added to the beginning of the file name without a pair")
    args = parser.parse_args()

    image_dir = args.images
    label_dir = args.labels

    images = os.listdir(image_dir)
    labels = os.listdir(label_dir)

    labels_without_extension = []
    images_without_extension = []

    symbol_change_to = '$'
    
    ending = ".jpg"

    for label in labels:
        if label.split('.')[-1] != "ini" and label.split('.')[-2] != "classes":
            labels_without_extension.append(".".join(label.split('.')[:-1]))

    for image in images:
        if image.split('.')[-1] != "ini":
            ending = image.split('.')[-1]
            images_without_extension.append(".".join(image.split('.')[:-1]))

    images_without_extension_count = 0
    for image_without_extension in images_without_extension:
        if image_without_extension[0] != '_' and  image_without_extension[0] != symbol_change_to:
            if image_without_extension not in labels_without_extension:
                images_without_extension_count += 1
                os.rename(str(os.path.join(image_dir, image_without_extension + "." + ending)),
                          str(os.path.join(image_dir, symbol_change_to + image_without_extension + "." + ending)))
        else:
            images_without_extension_count += 1

    labels_without_extension_count = 0
    for label_without_extension in labels_without_extension:
        if label_without_extension[0] != '_' and label_without_extension[0] != symbol_change_to:
            if label_without_extension not in images_without_extension:
                labels_without_extension_count += 1
                os.rename(str(os.path.join(label_dir, label_without_extension + ".txt")),
                          str(os.path.join(label_dir, symbol_change_to + label_without_extension + ".txt")))
        else:
            labels_without_extension_count += 1

    print(f"{images_without_extension_count}-images without label!"
          f"\n{labels_without_extension_count}-labels without image!")
