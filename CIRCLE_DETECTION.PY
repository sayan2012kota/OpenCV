import cv2
circles_image = cv2.imread(r"C:\Users\pooja\Desktop\OpenCV\circles.png", cv2.IMREAD_COLOR)
cv2.imshow("window", circles_image)
cv2.waitKey(0)
greyscale_circle = cv2.cvtColor("circles_image", cv2.COLOR_BGR2GRAY)
blurred_greyscale_circle = cv2.blur("greyscale_circle", (5,5))
detected_circles = cv2.HoughCircles(blurred_greyscale_circle, cv2.HOUGH_GRADIENT, 1, 25, param1=22, param2=1000,minRadius=1, maxradius=1000)
if len(detected_circles) > 0:
    for i in detected_circles:
        x=i[0]
        y=i[1]
        r=i[2]
        print(x,y,r)