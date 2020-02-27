import cv2
import numpy as np

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width)
print(height)

writer = cv2.VideoWriter('edges_test_video2.mp4',cv2.VideoWriter_fourcc(*'DVIX'),25,(width,height))

while 1:

  ret,frame = cap.read()
  med_val = np.median(frame)
  lower = int(max(0, 0.7* med_val))
  upper = int(min(255,1.3 * med_val))
  blurred_img = cv2.blur(frame,ksize=(4,4))
  edges = cv2.Canny(image=blurred_img, threshold1=lower , threshold2=upper)
  cv2.imshow('frames',edges)
  writer.write(edges)


  if cv2.waitKey(1) & 0xFF == ord('q'):
    break


cap.release()
writer.release()
cv2.destroyAllWindows()
