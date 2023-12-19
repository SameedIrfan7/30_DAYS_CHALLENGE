import cv2
import imutils


img=cv2.imread("f.jpg")

resize_img=imutils.resize(img,width=50)

cv2.imwrite("resizedimage.jpg",resize_img)