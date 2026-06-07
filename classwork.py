import cv2
import os
apple = cv2.imread("C:/Users/pooja/Desktop/OpenCV/apple.png", cv2.IMREAD_COLOR)
cv2.imshow("window", apple)
cv2.waitKey(0)
row = apple.shape[0]
column = apple.shape[1]
rotation_matrix =  cv2.getRotationMatrix2D((row/2, column/2),313, 1)
rotated_img = cv2.warpAffine(apple, rotation_matrix, (row, column))
cv2.imshow("rotated image", rotated_img)
cv2.waitKey(0)
edge_image = cv2.Canny(apple, 40, 60)
cv2.imshow("edge image", edge_image)
cv2.waitKey(0)
hsv = cv2.cvtColor(apple, cv2.COLOR_BGR2HSV)
cv2.imshow("hue saturation image", hsv)
cv2.waitKey(0)
starting_point = (50,50)
ending_point = (160, 160)
lined_image = cv2.line(apple, starting_point, ending_point, (246, 57, 197), 7)
cv2.imshow("drawing", lined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()