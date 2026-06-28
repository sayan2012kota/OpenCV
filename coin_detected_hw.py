import cv2
circle_image = cv2.imread(r"C:\Users\pooja\Desktop\OpenCV\circles.png", cv2.IMREAD_COLOR)
parameter = cv2.SimpleBlobDetector_Params()
parameter.filterByArea = True
parameter.minArea = 200
parameter.filterByCircularity = True
parameter.minCircularity = 0.8
parameter.filterByConvexity = True
parameter.minConvexity = 0.6
parameter.filterByInertia = True
parameter.minInertiaRatio = 0.7
blob_detector = cv2.SimpleBlobDetector_create(parameter)
detected_blobs = blob_detector.detect(circle_image)
cv2.drawKeypoints(circle_image, detected_blobs, circle_image, (0,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
font_family = cv2.FONT_HERSHEY_COMPLEX
location  = (0, 100)
amount = len(detected_blobs)
text = cv2.putText(circle_image,str(amount), location, font_family, 2, (0,0,0))
cv2.imshow("window", circle_image)
print(detected_blobs)
cv2.waitKey(0)