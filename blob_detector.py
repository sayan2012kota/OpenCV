import cv2
flower = cv2.imread(r"C:\Users\pooja\Desktop\OpenCV\circles.png", cv2.IMREAD_COLOR)
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
detected_blobs = blob_detector.detect(flower)
cv2.drawKeypoints(flower, detected_blobs, flower, (0,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("window", flower)
cv2.waitKey(0)