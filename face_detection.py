import cv2
import os
import numpy

haarfile = r"C:\Users\pooja\Desktop\OpenCV\face_recognition\haarcascade_frontalface_default.xml"
image_folder = r"C:\Users\pooja\Desktop\OpenCV\face_recognition\image"
all_images = []
numbers = []
dictionary = {}
zero = 0
for folder, subfolder, files in os.walk(image_folder):
    for i in subfolder:
        dictionary[zero] = i