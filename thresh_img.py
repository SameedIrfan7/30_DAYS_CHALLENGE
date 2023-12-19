import cv2

img=cv2.imread("f.jpg")
#read an image
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#convert into gray_scale image
thres=cv2.threshold(gray,190,255,cv2.THRESH_BINARY)[1]
#converting into threshold valued 
# #190-threshold limit
# #255-is given color 
# #cv2.Thresh_BINARY is a function accessing from it 
# #[1]it 2 values by taking gray and saving the threshold image in path
cv2.imwrite("threshold190.jpg",thres)
#saving the image