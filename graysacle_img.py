import cv2 #importing library

img=cv2.imread("f.jpg")
#accessing the image
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#color to gray_scale

cv2.imwrite("grayImage.png",gray)
#saving gray_scale_img same path
cv2.imshow("Original",img)
#display org_img 
cv2.imshow("Gray",gray)
#displaying gray_img
cv2.waitKey(0)
#it denotes for us to enter any ky to exit an display till that it displays
cv2.destroyAllWindows()
#it destroys/stops all current running tabs and display the image until i exit
