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
    x,y = image.size
    sum = sum+x
    height_sum = height_sum + y
mean_width = sum/5
mean_height  = height_sum/5
for i in images:
    path = os.path.join(images_path, i)
    stored_image  = Image.open(path)
    mean_height = int(mean_height)
    mean_width = int(mean_width)
    resized_image = stored_image.resize((mean_width, mean_height))
    resized_image.save(i, "JPEG", quality = 100)
video  = "images_video.mp4"
os.chdir(images_path)

generated_video = cv2.VideoWriter(video, cv2.VideoWriter_fourcc(*"mp4V"), 1, (mean_width, mean_height))
for e in images:
    generated_video.write(cv2.imread(os.path.join(images_path, e)))
generated_video.release()
