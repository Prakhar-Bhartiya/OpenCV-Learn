import numpy as np
import cv2

# Parameters for ShiTomasi corner detection (good features to track paper)
corner_track_params = dict(maxCorners = 15,
                       qualityLevel = 0.4,
                       minDistance = 7,
                       blockSize = 7 )


 # Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (200,200),maxLevel = 2,criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10,0.03))



cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width)
print(height)

writer = cv2.VideoWriter('object_tracking.mp4',cv2.VideoWriter_fourcc(*'DVIX'),30,(width,height))
ret, prev_frame = cap.read()

prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)


prevPts = cv2.goodFeaturesToTrack(prev_gray, mask = None, **corner_track_params)

                                         # Create a matching mask of the previous frame for drawing on later
mask = np.zeros_like(prev_frame)


while True:

  ret,frame = cap.read()

                                             # Grab gray scale
  frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  nextPts, status, err = cv2.calcOpticalFlowPyrLK(prev_gray, frame_gray, prevPts, None, **lk_params)

                                             # Using the returned status array (the status output)
                                             # status output status vector (of unsigned chars); each element of the vector is set to 1 if
                                             # the flow for the corresponding features has been found, otherwise, it is set to 0.
  good_new = nextPts[status==1]
  good_prev = prevPts[status==1]

                                             # Use ravel to get points to draw lines and circles
  for i,(new,prev) in enumerate(zip(good_new,good_prev)):

    x_new,y_new = new.ravel()
    x_prev,y_prev = prev.ravel()

                                                 # Lines will be drawn using the mask created from the first frame
    mask = cv2.line(mask, (x_new,y_new),(x_prev,y_prev), (0,255,0), 3)

                                                 # Draw red circles at corner points
    frame = cv2.circle(frame,(x_new,y_new),8,(0,0,255),-1)

                                             # Display the image along with the mask we drew the line on.
    img = cv2.add(frame,mask)

    cv2.imshow('frame',img)

  writer.write(img)
  k = cv2.waitKey(30) & 0xff
  if k == 27:
      break

                                             # Now update the previous frame and previous points
  prev_gray = frame_gray.copy()
  prevPts = good_new.reshape(-1,1,2)


cv2.destroyAllWindows()
cap.release()
