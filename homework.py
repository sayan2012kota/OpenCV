import cv2
import os
image = cv2.imread(r"C:\Users\pooja\Desktop\OpenCV\flower.png", cv2.IMREAD_COLOR)
cv2.imshow("Original Image", image)
cv2.waitKey(0)
os.chdir(r"C:\Users\pooja\Desktop\OpenCV\images")
cv2.imwrite("flower.png", image)