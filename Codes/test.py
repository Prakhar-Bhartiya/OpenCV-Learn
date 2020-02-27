import cv2
import numpy as np
import matplotlib.pyplot as ptt
%matplotlib inline



#img = cv2.imread('test.jpg')
white_n = np.random.randint(low=0,high=2,size=(600,600))
while 1:
   cv2.imshow('test',white_n)

  #if cv2.waitKey(1) & 0xFF == 27 :
     #break


cv2.destroyAllWindows()

print(img.shape)
print("heee")
