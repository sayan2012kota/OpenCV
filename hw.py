import cv2
import os
image = cv2.imread(r"C:\Users\pooja\Desktop\OpenCV\images\field.png", cv2.IMREAD_COLOR)
image2 = cv2.imread(r"C:\Users\pooja\Desktop\OpenCV\images\abstract_image.png", cv2.IMREAD_COLOR)
resized_field = cv2.resize(image, (2000, 1334))
combined_image = cv2.addWeighted(image2, 0.6, resized_field, 0.4, 0)
cv2.imshow("window", combined_image)
cv2.waitKey(0)