import numpy as np
import cv2 as cv

from keras.models import load_model

newmodel = load_model('mnist_model.h5')

img = cv.imread('images.jpg')

print(img.shape)

print(newmodel.predict_classes(img))
