import os
import argparse



def count(directory):
    classes = dict()
    classnames = dict()
    
    parser = argparse.ArgumentParser(description='Count of labels (OBB format) for each class recursive')
    parser.add_argument('--root_dir', "-d", help="Root directory of deleting")
    args = parser.parse_args()
    directory_path = args.root_dir
    
    print(f"{os.path.abspath(directory_path)} result:")
    for root,paths, files in os.walk(directory_path):
        for file in files:
            if file == "classes.txt":
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    for i in range(len(lines)):
                        classnames[i] = lines[i][:-1]
                continue
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    if(len(lines)>0):
                        if(not "YOLO_OBB" in lines[0]):
                            pass
                            # print(f"NOT OBB")
                        else:
                            for i in range(1, len(lines)):
                                words = lines[i].split()
                                if words[0] not in classes.keys():
                                    classes[words[0]] = 1
                                else:
                                    classes[words[0]] += 1
    for key in classnames.keys():
        count = 0
        if str(key) in classes.keys():
            count = classes[str(key)]
            
        printedClassName = classnames[key]
        printedClassName = printedClassName.ljust(25)
        print(f"{printedClassName}\t|\t{count}")
