import cv2

cat_image = cv2.imread(r"C:\Users\pooja\Desktop\OpenCV\cat_image.jpg")
cascade =  cv2.CascadeClassifier(r"C:\Users\pooja\Desktop\OpenCV\haarcascade_frontalcatface.xml")
image = cat_image
coloured_image = image
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face_coordinates = cascade.detectMultiScale(image, 1.15, 1)
for x, y, w, h in face_coordinates:
    cv2.rectangle(coloured_image, (x, y), (x+w, y+h), (0, 255, 24), 2)
cv2.imshow("window", coloured_image)
cv2.waitKey(0)
