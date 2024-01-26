import shutil
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

def similarity_test():
    parser = argparse.ArgumentParser(
        description='Analyzes the structure of the images and discards those that have copies in the set to a separate directory')

    parser.add_argument('--source_images', "-i", type=dir_path, help="source images directory")
    parser.add_argument('--threshold', "-t", type=float, help="threshold of similarity (everything above is thrown into the 'duplicates' folder )")
    parser.add_argument('--dublicates', "-d", type=str, help="the folder where the copies are dumped")

    args = parser.parse_args()
    threshold = float(args.threshold)
    source_images = args.source_images
    dublicates = args.dublicates


    images_names =  [ ] 
    for image in os.listdir(source_images):
        if os.path.isfile(os.path.join(source_images,image)):
            images_names.append( image  )
    print(len(images_names))

    encoded_image = model.encode([Image.open(os.path.join(source_images,    filepath)) for filepath in images_names], batch_size=8, convert_to_tensor=True, show_progress_bar=True)
    processed_images = util.paraphrase_mining_embeddings(encoded_image)

    if not os.path.exists( dublicates ):
        os.mkdir(dublicates )
    targetPath = dublicates

    duplicates_images = [image for image in processed_images if image[0] >= threshold]
    print(f"count of dublicates: {len(duplicates_images)}")
    print(duplicates_images)
    for score, image_id1, image_id2 in duplicates_images:
        if os.path.isfile(os.path.join(source_images,images_names[image_id2])):
            shutil.move ( os.path.join(source_images,images_names[image_id2]), os.path.join(targetPath, images_names[image_id2]  ))