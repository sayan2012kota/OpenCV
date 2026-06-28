import cv2
import os
from PIL import Image
images_path = r"C:\Users\pooja\Desktop\OpenCV\video_images"
os.chdir(images_path)
mean_width = 0
mean_height = 0
images = []
sum = 0
height_sum = 0
for i in os.listdir("."):
    if i.endswith((".png", ".jpg")):
        images.append(i)
print(images)
for r in images:
    image= Image.open(os.path.join(images_path, r))
    x,y = image.sized
    sum = sum+x
    height_sum = height_sum + y
mean_width = sum/5
mean_height  = height_sum/5