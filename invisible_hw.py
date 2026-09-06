import cv2
import numpy as np
video = cv2.VideoCapture(r"C:\Users\pooja\Desktop\OpenCV\VID_20260906_084637.mp4")
background = None

for i in range(10):
    boolean, frame = video.read()
    if boolean == True:
        background = frame
flipped_background = np.flip(background, axis = 1)
print(flipped_background)
while video.isOpened():
    boolean2, frames = video.read()
    print(boolean2)
    flipped_frame = np.flip(frames, axis = 1)
    image =  cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2HSV)
    lower_yellow_range = np.array([15, 30, 100])
    higher_yellow_range = np.array([45, 255, 255])
    mask = cv2.inRange(image, lower_yellow_range, higher_yellow_range)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations=1)
    mask2 = cv2.bitwise_not(mask)
    result1 = cv2.bitwise_and(background, background, mask=mask)
    result2 = cv2.bitwise_and(flipped_frame, flipped_frame,  mask=mask2)
    final_image = cv2.addWeighted(result1, 1, result2, 1, 0)
    cv2.imshow("window", final_image)
    cv2.waitKey(10)
    print("o")