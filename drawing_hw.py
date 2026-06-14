import cv2
import os
road = cv2.imread("C:/Users/pooja/Desktop/OpenCV/road.png", cv2.IMREAD_COLOR)
starting_point = (0,0)
ending_point = (212,159)
lined_road = cv2.line(road, starting_point, ending_point, (0,0,255), 5)
cv2.imshow("window", lined_road)
cv2.waitKey(0)
crossed_road = cv2.line(lined_road, (212,0), (0,159), (0,0,255), 5)
cv2.imshow("crossed  out road", crossed_road)
cv2.waitKey(0)
cv2.destroyAllWindows()