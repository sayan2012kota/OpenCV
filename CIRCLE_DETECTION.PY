import cv2
import numpy as np
circles_image = cv2.imread(r"C:\Users\pooja\Desktop\OpenCV\images\img.png", cv2.IMREAD_COLOR)
cv2.imshow("window", circles_image)
cv2.waitKey(0)
greyscale_circle = cv2.cvtColor(circles_image, cv2.COLOR_BGR2GRAY)
blurred_greyscale_circle = cv2.blur(greyscale_circle, (5,5))
detected_circles = cv2.HoughCircles(blurred_greyscale_circle, cv2.HOUGH_GRADIENT, 1, 25, param1=30,param2=50,minRadius=20, maxRadius=100)
detected_circles = np.uint16(np.around(detected_circles))
print(detected_circles)
if len(detected_circles) is not None:
    for i in detected_circles[0, :]:
        x=i[0]
        y=i[1]
        r=i[2]
        circle =cv2.circle(circles_image,(x,y),r, (0,0,0), 10)
        cv2.imshow("window", circles_image)
        cv2.waitKey(0)