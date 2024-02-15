import os
import argparse
from sentence_transformers import SentenceTransformer, util
from PIL import Image
import os


def dir_path(string:str):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

def sorted_filesizes(source_folder, sort):
    file_sizes = {}
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                file_path = os.path.relpath(os.path.join(root, file), start=source_folder)
                file_sizes[file_path] = os.path.getsize(os.path.join(source_folder, file_path))
    print(f"Sorting status {sort}")
    if sort:
        file_sizes = dict(sorted(file_sizes.items(), key=lambda item: item[1], reverse=True))
    else:
        file_sizes = dict(sorted(file_sizes.items(), key=lambda item: item[0]))
    result = []
    for key, value in file_sizes.items():
        result.append([key, value])
    print(f"Finished creation of filelist, appended {len(result)} candidats")
    return result

def decimator():
    parser = argparse.ArgumentParser(
        description='Analyzes the structure of the images and discards those that have copies in the set to a separate directory')

    parser.add_argument('--source_images', "-d", type=dir_path, help="source images directory")
    parser.add_argument('--threshold', "-t", type=float, help="threshold of similarity (everything above is thrown into the 'duplicates' folder )")
    parser.add_argument('--sort','-s',action='store_true', help="Sort by size files during process")
    
    
    
    args = parser.parse_args()
    
    sort = args.sort
    threshold = float(args.threshold)
    source_images = args.source_images


    
    
    data = sorted_filesizes(source_images, sort)
    model = SentenceTransformer('clip-ViT-B-32')
    totalLen  = len(data)
    counter = 0
    delcounter = 0
    compareToImage = None



    print("Starting process...")
    for file,_ in data:
        if not compareToImage:
            compareToImage = Image.open(os.path.join(source_images, file))
            continue
        else:
            try:
                current  = Image.open( os.path.join(source_images, file))
                encoded_image = model.encode([current, compareToImage], batch_size=8, convert_to_tensor=True)
                processed_images = util.paraphrase_mining_embeddings(encoded_image)
                if(processed_images[0][0] > threshold):
                    print(f"Deleting {os.path.join(source_images, file)}. Deleted total {delcounter} and {totalLen-counter} left")
                    os.remove(  os.path.join(source_images, file))
                    delcounter+=1
                    
                counter += 1
                compareToImage = current
            except Exception as E:
                print(str(E))