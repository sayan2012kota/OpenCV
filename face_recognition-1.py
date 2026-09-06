import cv2
import os

haarfile = r"C:\Users\pooja\Desktop\OpenCV\face_recognition\haarcascade_frontalface_default.xml"
image = r"C:\Users\pooja\Desktop\OpenCV\face_recognition\image"
sayan = r"C:\Users\pooja\Desktop\OpenCV\face_recognition\image\sayan"
new_folder_path = os.path.join(image, "sayan")
if not os.path.isdir(new_folder_path):
    os.mkdir(new_folder_path)
height = 100
width = 150
cascade_classifier = cv2.CascadeClassifier(haarfile)
webcam = cv2.VideoCapture(0)
for i in range(30):
    boolean, images = webcam.read()
    images = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
    face_coordinates = cascade_classifier.detectMultiScale(images, 1.5, 4)
    print(face_coordinates)
