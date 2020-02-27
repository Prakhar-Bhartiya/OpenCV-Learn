import cv2
import numpy as np

face = cv2.imread('test_face.jpg',0)
sift = cv2.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(face,None)

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width)
print(height)


writer = cv2.VideoWriter('edges_test_video2.mp4',cv2.VideoWriter_fourcc(*'DVIX'),25,(width,height))

while 1:

    ret,frame = cap.read()

    kp2, des2 = sift.detectAndCompute(frame,None)

    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)

    flann = cv2.FlannBasedMatcher(index_params,search_params)

    matches = flann.knnMatch(des1,des2,k=2)

    good = []

# ratio test
    for i,(match1,match2) in enumerate(matches):
        if match1.distance < 0.7*match2.distance:
            good.append([match1])

    flann_matches = cv2.drawMatchesKnn(face,kp1,frame,kp2,good,None,flags=0)

    cv2.imshow('frames',flann_matches)
    writer.write(edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
writer.release()
cv2.destroyAllWindows()
