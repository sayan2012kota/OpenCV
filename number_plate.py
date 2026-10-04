import cv2

car_video = cv2.VideoCapture(r"C:\Users\pooja\Desktop\OpenCV\cars3.mp4")
cascade = cv2.CascadeClassifier(r"C:\Users\pooja\Desktop\OpenCV\haarcascade_license_plate_rus_16stages.xml")

while True:
    boolean, images = car_video.read()
    coloured_image = images
    images = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
    number_plate_coords = cascade.detectMultiScale(images, 1.1, 1)
    for x, y, w, h in number_plate_coords:
        cv2.rectangle(coloured_image, (x, y), (x+w, y+h), (255, 140, 37), 3)
    cv2.imshow("window", coloured_image)
    s = cv2.waitKey(10)
    if s == 115:
        break
