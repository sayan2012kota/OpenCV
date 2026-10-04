import cv2
import os

car_video = cv2.VideoCapture(r"C:\Users\pooja\Desktop\OpenCV\Cars.mp4")
cascade = cv2.CascadeClassifier(r"C:\Users\pooja\Desktop\OpenCV\cars.xml")
while True:
    boolean, image = car_video.read()
    coloured_img = image
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    car_coordinates =  cascade.detectMultiScale(image, 1.1, 1)
    for x,y,w,h in car_coordinates:
        cv2.rectangle(coloured_img, (x, y), (x+w, y+h), (92, 65, 255), 5)
    cv2.imshow("window", coloured_img)
    s = cv2.waitKey(10)
    if s == 115:
        break