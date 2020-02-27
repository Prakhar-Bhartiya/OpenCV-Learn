import numpy as np
import cv2
import matplotlib.pyplot as plt

face_cascade = cv2.CascadeClassifier('C:/Users/91740/Desktop/Computer-Vision-with-Python/DATA/haarcascades/haarcascade_frontalface_default.xml')


def detect_face(img):

    face_img = img.copy()

    face_rects = face_cascade.detectMultiScale(face_img,scaleFactor=1.2, minNeighbors=5)

    for (x,y,w,h) in face_rects:
        cv2.rectangle(face_img, (x,y), (x+w,y+h), (255,255,255), 5)

    return face_img


eye_cascade = cv2.CascadeClassifier('C:/Users/91740/Desktop/Computer-Vision-with-Python/DATA/haarcascades/haarcascade_eye.xml')

def detect_eyes(img):

    face_img = img.copy()

    eyes = eye_cascade.detectMultiScale(face_img,scaleFactor=1.2, minNeighbors=5)


    for (x,y,w,h) in eyes:
        cv2.rectangle(face_img, (x,y), (x+w,y+h), (255,255,255), 5)

    return face_img

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width)
print(height)

writer = cv2.VideoWriter('face_detect_withglass.mp4',cv2.VideoWriter_fourcc(*'DVIX'),25,(width,height))

while True:

    ret, frame = cap.read(0)

    frame = detect_face(frame)  #change here to get different variants of detection
    writer.write(frame)
    cv2.imshow('Video Face Detection', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
