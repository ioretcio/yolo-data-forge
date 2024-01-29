import os
import argparse
from sentence_transformers import SentenceTransformer, util
from PIL import Image
import os

model = SentenceTransformer('clip-ViT-B-32')
def dir_path(string:str):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

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

def decimator():
    parser = argparse.ArgumentParser(
        description='Analyzes the structure of the images and discards those that have copies in the set to a separate directory')

    parser.add_argument('--source_images', "-d", type=dir_path, help="source images directory")
    parser.add_argument('--threshold', "-t", type=float, help="threshold of similarity (everything above is thrown into the 'duplicates' folder )")

    
    
    args = parser.parse_args()
    threshold = float(args.threshold)
    source_images = args.source_images


    
    
    data = sorted_filesizes(source_images)
    totalLen  = len(data)
    counter = 0
    delcounter = 0




    print("Starting process...")
    for file,_ in data:
        if not compareToImage:
            compareToImage = Image.open(os.path.join(source_images, file))
            continue
        else:
            try:
                if(counter %1000 == 0):
                    print(f"{counter} ~ {round(100*(counter/totalLen ))}%, {delcounter} deleted")
                current  = Image.open( os.path.join(source_images, file))
                encoded_image = model.encode([current, compareToImage], batch_size=8, convert_to_tensor=True)
                processed_images = util.paraphrase_mining_embeddings(encoded_image)
                if(processed_images[0][0] > threshold):
                    os.remove(  os.path.join(source_images, file))
                    delcounter+=1
                else:
                    os.remove(os.path.join(source_images, file))
                counter += 1
                compareToImage = current
            except Exception as E:
                print(str(E))