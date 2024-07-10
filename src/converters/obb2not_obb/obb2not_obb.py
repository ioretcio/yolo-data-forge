import os
import cv2
import argparse
import math

classes = dict()


def rotate_point(origin, point, angle):
    ox, oy = origin
    px, py = point
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


def generatePoints(label):
    if label[0] == "YOLO_OBB":
        return
    centerX = float(label[1])
    centerY = float(label[2])
    width = float(label[3])
    height = float(label[4])
    angle = -(math.pi * float(label[5]) / 180)
    bottom_left = (centerX - width / 2, centerY - height / 2)
    bottom_right = (centerX + width / 2, centerY - height / 2)
    top_right = (centerX + width / 2, centerY + height / 2)
    top_left = (centerX - width / 2, centerY + height / 2)
    bottom_left = rotate_point((centerX, centerY), bottom_left, angle)
    bottom_right = rotate_point((centerX, centerY), bottom_right, angle)
    top_right = rotate_point((centerX, centerY), top_right, angle)
    top_left = rotate_point((centerX, centerY), top_left, angle)

    return [bottom_left, bottom_right, top_right, top_left]


def convert():
    parser = argparse.ArgumentParser(
        description="Finds images and labels without a pair in the image-labels directories."
    )
    parser.add_argument("--images", "-i", help="images directory")
    parser.add_argument("--labels", "-l", help="labels directory")
    parser.add_argument("--newlabels", "-r", help="labels result directory")
    args = parser.parse_args()

    image_dir = args.images
    label_dir = args.labels
    labels_new_path = args.newlabels

    if not os.path.exists(labels_new_path):
        os.mkdir(labels_new_path)
    for label in os.listdir(label_dir):
        if label == "classes.txt" or label == "desktop.ini":
            continue
        with open(f"{label_dir}/{label}", "r") as f:
            with open(f"{labels_new_path}/{label}", "w") as w:
                image_extensions = ["jpg", "jpeg", "png", "PNG", "JPEG", "JPG"]
                image_path = None
                for ext in image_extensions:
                    if os.path.exists(
                        f"{image_dir}/{'.'.join(label.split('.')[:-1])}.{ext}"
                    ):
                        image_path = (
                            f"{image_dir}/{'.'.join(label.split('.')[:-1])}.{ext}"
                        )
                        break

                if image_path is not None:
                    image = cv2.imread(image_path)
                    hhh, www, _ = image.shape
                else:
                    print(f"Image not found for label: {label}")
                    continue

                lines = [line.split() for line in f.readlines()]
                for i in range(1, len(lines)):
                    points = generatePoints(lines[i])
                    x_values = [point[0] for point in points]
                    y_values = [point[1] for point in points]
                
                    center_x = ((min(x_values) + max(x_values)) / 2)/www
                    center_y = ((min(y_values) + max(y_values)) / 2)/hhh
                    relwidth = (max(x_values) - min(x_values)) / www
                    relheight = (max(y_values) - min(y_values)) / hhh
                    line = f"{lines[i][0]} {center_x} {center_y} {relwidth} {relheight}\n"
                    w.write(line)
