import cv2
import numpy as np
video = cv2.VideoCapture(r"C:\Users\pooja\Desktop\OpenCV\images\Invisible man video.mp4")
background = None

for i in range(10):
    boolean, frame = video.read()
    if boolean == True:
        background = frame
#video.release()
flipped_background = np.flip(background, axis = 1)
print(flipped_background)
while video.isOpened():
    boolean2, frames = video.read()
    print(boolean2)
    flipped_frame = np.flip(frames, axis = 1)
    image =  cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2HSV)
    red_values = np.array([0, 120, 40])
    highest_red_value = np.array([100, 255, 255])
    mask = cv2.inRange(image, red_values, highest_red_value)
    lower_red_range = np.array([170, 40, 40])
    highest_red_range = np.array([180, 255, 255])
    mask2 = cv2.inRange(image, lower_red_range, highest_red_range)
    mask = mask + mask2
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations=1)
    mask2 = cv2.bitwise_not(mask)
    result1 = cv2.bitwise_and(background, background, mask=mask)
    result2 = cv2.bitwise_and(flipped_frame, flipped_frame,  mask=mask2)
    final_image = cv2.addWeighted(result1, 1, result2, 1, 0)
    cv2.imshow("window", final_image)
    cv2.waitKey(10)
    print("o")