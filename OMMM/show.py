import cv2
import numpy as np
import pyautogui
import time

path = '../happy/testpicture/test1.png'

img = cv2.imread(path)

cv2.imshow('image', img)
resize_img = cv2.resize(img, (1080, 1080))
cv2.imshow('resize', resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()