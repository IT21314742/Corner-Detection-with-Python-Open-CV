import numpy as np
import cv2

img = cv2.imread('assets/chessboard.png')



cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()