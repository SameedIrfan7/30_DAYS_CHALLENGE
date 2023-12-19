import cv2


# reading an image
img = cv2.imread("f.jpg")

# saving an image
cv2.imwrite("farwell1.png", img)

# display an image
cv2.imshow("a", img)

cv2.waitKey(0)

cv2.destroyAllWindows()
