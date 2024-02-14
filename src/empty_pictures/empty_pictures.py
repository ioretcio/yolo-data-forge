import os
import argparse
import time

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
    
    args = parser.parse_args()

    image_dir = args.images
    label_dir = args.labels

    images = os.listdir(image_dir)
    labels = os.listdir(label_dir)

    labels_dict = {}
    images_dict = {}


    start_time = time.time()
    print("Forming labels list")
    for label in labels:
        splitted = label.split('.')
        if "ini" in splitted: continue
        if "current_config" in splitted: continue
        if "classes" in splitted: continue
        if len(splitted)<2: print(f"No extension in file {label}") 
        labels_dict[".".join(label.split('.')[:-1])] = label
    print(f"Labels list formed in {time.time() - start_time} seconds")
    
    
    
    
    start_time = time.time()
    print("Forming images list")
    for image in images:
        if image.split('.')[-1] != "ini":
            images_dict[".".join(image.split('.')[:-1])] = image
    print(f"Images list formed in {time.time() - start_time} seconds")
    
    
    
    
    start_time = time.time()
    print("Processing images without pair")
    images_without_extension_count = 0
    for image_without_extension in images_dict.keys():
        if image_without_extension not in labels_dict.keys():
            images_without_extension_count += 1
            
            if not os.path.exists(os.path.join(image_dir, "single")):
                os.mkdir(os.path.join(image_dir, "single"))
                
            os.rename(str(os.path.join(image_dir, images_dict[image_without_extension])),
                        str(os.path.join(image_dir,"single", images_dict[image_without_extension])))
    print(f"Images without labels moved in {time.time() - start_time} seconds")
    
    
    start_time = time.time()
    print("Processing images without pair")
    labels_without_extension_count = 0
    for label_without_extension in labels_dict.keys():
        if label_without_extension not in images_dict.keys():
            labels_without_extension_count += 1
            
            if not os.path.exists(os.path.join(label_dir, "single")):
                os.mkdir(os.path.join(label_dir, "single"))
                
            os.rename(str(os.path.join(label_dir, labels_dict[label_without_extension])),
                        str(os.path.join(label_dir,"single", labels_dict[label_without_extension])))
    print(f"Labels without images moved in {time.time() - start_time} seconds")
    print()
    print(f"{images_without_extension_count}-images without label!"
          f"\n{labels_without_extension_count}-labels without image!")
    print(f'All result moved to {os.path.join(label_dir, "single")} and {os.path.join(image_dir, "single")} folders')