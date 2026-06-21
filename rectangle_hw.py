import cv2
import os
blank_background = cv2.imread(r"C:\Users\pooja\Desktop\OpenCV\images\blank_background.png", cv2.IMREAD_COLOR)
resized_background = cv2.resize(blank_background, (1000,1300))
rectangle  = cv2.rectangle(resized_background,  (30, 30), (950, 1250), (0,0,0), 10)
circle = cv2.circle(resized_background, (470, 250), 200, (0,0,255), -1)
circle2 = cv2.circle(resized_background, (470, 650), 200, (0,255,255), -1)
circle3 = cv2.circle(resized_background, (470,1050), 200, (0,255,0), -1)
cv2.imshow("window", resized_background)
cv2.waitKey(0)
cv2.destroyAllWindows()