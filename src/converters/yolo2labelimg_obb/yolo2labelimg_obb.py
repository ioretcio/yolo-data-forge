import os
import math
import argparse

def center(first_dot, second_dot):
    return (second_dot + first_dot) / 2

def convert():
    parser = argparse.ArgumentParser(description='Converts yolo_obb format to labelimg_obb')
    parser.add_argument('--labels_source','-s'  ,type=str, help='path to the labels directory')
    parser.add_argument('--labels_destination','-d' ,type=str, help='path to the new labels directory')
    args = parser.parse_args()
    labels_path = args.labels_source
    labels_new_path = args.labels_destination
    
    
    if not os.path.exists(labels_new_path):
        os.mkdir(labels_new_path)
    count = 0
    for label in os.listdir(labels_path):
        count+=1
        if(count%1000==0):
            print(count)
        with open(f"{labels_path}/{label}", "r") as f:
            with open(f"{labels_new_path}/{label}", "w") as w:
                lines = [line.split() for line in f.readlines()]
                w.write("YOLO_OBB\n")
                for object in lines:
                    class_id, x1, y1, x2, y2, x3, y3, x4, y4 = (object[0]),\
                        float(object[1]), float(object[2]), float(
                        object[3]), float(object[4]), float(object[5]),\
                            float(object[6]), float(object[7]), float(object[8])

                    first_line = math.sqrt(
                        math.pow((x2 - x1), 2) + (math.pow((y2 - y1), 2)))
                    second_line = math.sqrt(
                        math.pow((x3 - x2), 2) + (math.pow((y3 - y2), 2)))

                    height = second_line
                    width = first_line
                    x_center = center(x1, x3)
                    y_center = center(y1, y3)
                    hypotenuse = math.sqrt(
                        math.pow((x4 - x3), 2) + (math.pow((y4 - y3), 2)))
                    cathetus = x3 - x4

                    if(hypotenuse != 0):
                        angle = 90 + \
                            math.degrees(math.acos(cathetus / hypotenuse))
                        if (y1 < y2):

                            angle = 90 - \
                                math.degrees(math.acos(cathetus / hypotenuse))
                    else:
                        angle = 0
                    line = f"{class_id} {x_center} {y_center} {height} {width} {angle}"
                    w.write(line + "\n")
