import cv2
img=cv2.imread("f.jpg")

blur=cv2.GaussianBlur(img,(21,21),0)

cv2.imwrite("gussianimage.jpg",blur)