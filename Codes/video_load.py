import cv2
import time

cap = cv2.VideoCapture('video.mp4')

if cap.isOpened() == False:
  print("Error!!!")

while cap.isOpened():

  ret,frame = cap.read()

  if ret == True:


      time.sleep(1/25)
      cv2.imshow('frames',frame)

      if cv2.waitKey(1) & 0xFF == ord('q'):
          break

  else:
      break


cap.release()
cv2.destroyAllWindows()
