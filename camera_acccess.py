import cv2
vs=cv2.VideoCapture(0)
while True:
    _,img=vs.read()#read the frames from camera
    #like wise yestrerday to passthe 2 parameters we did smthg like this[1], _,(this is also an one alternative way)
    cv2.imshow("VideoStream",img)#display frames
    #below line, frame will show continously until we press q word
    key=cv2.waitKey(1) & 0xFF#record my key press- Hexadecimal
    if key ==ord("q"):
        break # breaking the infinite loop
    
vs.release() #release the camera
cv2.destroyAllWindows()#all opened windows will be closed
    