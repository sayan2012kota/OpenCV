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
        subfolder_path = os.path.join(image_folder, i)
        for r in os.listdir(subfolder_path):
            image_path = os.path.join(subfolder_path, r)
            image = cv2.imread(image_path, 0)
            image = cv2.resize(image, (220, 220))
            all_images.append(image)
            numbers.append(zero)
        zero = zero + 1
all_images = numpy.array(all_images)
numbers = numpy.array(numbers)
model = cv2.face.LBPHFaceRecognizer_create()
model.train(all_images, numbers)
cascade_classifier = cv2.CascadeClassifier(haarfile)
webcam = cv2.VideoCapture(0)
while True:
    boolean, images = webcam.read()
    face_coordinates = cascade_classifier.detectMultiScale(images, 1.05, 2)
    #print(face_coordinates)
    for x, y, w, l in face_coordinates:
        cropped_face = images[y:y+l, x:x+w]
        prediction = model.predict(cropped_face)
        #print(prediction)