import argparse
import os
import shutil

def dir_path(string):
    if os.path.isdir(string): return string
    else: raise NotADirectoryError(string)

extensions = ['jpg', 'png', 'JPG']
zfil = 4

def ends(file):
    for extension in extensions:
        if(file.endswith(extension)):
            return True
    return False

def main(images_folder,labels_folder, countInFolder):
    images = []
    for image in os.listdir(images_folder):
        if os.path.isfile(os.path.join(images_folder,image)) and ends(image):
            images.append( image  )
    print(f"Images count {len(images)}")
    
    createdFolderIndex = 1
    while(True):
        print(f"Processing {createdFolderIndex} folder...")
        
        images_target_current = os.path.join(os.path.split(os.path.abspath(os.getcwd()))[-1]+str(createdFolderIndex).zfill(zfil), "images")
        labels_target_current = os.path.join(os.path.split(os.path.abspath(os.getcwd()))[-1]+str(createdFolderIndex).zfill(zfil), "labels" )
        
        createdFolderIndex+=1
        
        if not os.path.exists( images_target_current):
            os.makedirs(images_target_current)
        if not os.path.exists( labels_target_current):
            os.makedirs(labels_target_current)
        
        
        
        already=0
        for image in os.listdir(images_target_current):
            if os.path.isfile(os.path.join(images_target_current,image)) and ends(image):
                already+=1
        
        for i in range(already, countInFolder):
            
            shutil.move (  os.path.join(images_folder, images[0]), os.path.join( images_target_current,images[0] ))
            filename, file_extension = os.path.splitext( images[0])
            if os.path.exists( os.path.join(labels_folder, f"{filename}.txt" )):
                if not os.path.exists( os.path.join(labels_target_current, f"{filename}.txt" )):
                    shutil.move (  os.path.join(labels_folder, f"{filename}.txt" ), os.path.join( labels_target_current,f"{filename}.txt" ))


            images = images[1:]
            if not len(images):
                break
        
        if not len(images):
            break
        

def packer():
    parser = argparse.ArgumentParser( description='Can split big folders into npacs' )
    parser.add_argument('--imput', "-i", type=dir_path, help="source directory images")
    parser.add_argument('--ilput', "-l", type=dir_path, help="source directory labels")
    parser.add_argument('--count', "-c", type=str, help="count of object in one subfolder")
    args = parser.parse_args()
    images_folder = args.imput
    labels_folder = args.ilput
    countInFolder = int(args.count)
    main(images_folder, labels_folder, countInFolder)
