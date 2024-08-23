import numpy as np
import cv2

img = cv2.imread('assets/chessboard.png')
img = cv2.resize(img, (0, 0), fx=0.75)


cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()