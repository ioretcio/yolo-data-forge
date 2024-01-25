import argparse
import os
from PIL import Image

Image.MAX_IMAGE_PIXELS = None


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

def split4(image, image_path, image_new_path):
    im = Image.open(os.path.join(image_path, image))
    img_width, img_height = im.size

    patch_width = img_width//2
    patch_height = img_height//2

    piece = im.crop((0, 0, patch_width, patch_height))
    img = Image.new('RGB', (patch_width, patch_height), 255)
    img.paste(piece)
    path = os.path.join(image_new_path, f"{image.split('.')[0]}-{0}.png")
    img.save(path)

    piece = im.crop((patch_width, 0, img_width, patch_height))
    img = Image.new('RGB', ( img_width-patch_width, patch_height), 255)
    img.paste(piece)
    path = os.path.join(image_new_path, f"{image.split('.')[0]}-{1}.png")
    img.save(path)

    piece = im.crop((0, patch_height, patch_width, img_height))
    img = Image.new('RGB', (patch_width, img_height- patch_height), 255)
    img.paste(piece)
    path = os.path.join(image_new_path, f"{image.split('.')[0]}-{2}.png")
    img.save(path)

    piece = im.crop((patch_width, patch_height, img_width, img_height))
    img = Image.new('RGB', (img_width- patch_width,img_height-patch_height), 255)
    img.paste(piece)
    path = os.path.join(image_new_path, f"{image.split('.')[0]}-{3}.png")
    img.save(path)

    print(os.path.join(image_path, image) + ' done ')
def big_image_to4parts():
    parser = argparse.ArgumentParser(
        description='Divides the high resolution image into 4 equal pieces')
    parser.add_argument('--images', "-i", type=dir_path, help="images directory")
    parser.add_argument('--save', "-s", type=dir_path, help="save images directory")
    args = parser.parse_args()
    image_path = args.images
    image_new_path = args.save
    if not os.path.exists(image_new_path):
        os.mkdir(image_new_path)
    for image in os.listdir(image_path):
        split4(image, image_path, image_new_path)







