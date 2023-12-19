import cv2
import time
import imutils
#importing libraries

cam=cv2.VideoCapture(0)#accessing cameras
time.sleep(1)#giving 1 second delay

firstframe=None#make first frame nthg
area=800#threshold for how much chnage can be noticed in moving object

while True:
    _,img=cam.read()#read frames
    text="Normal"#if no moving object is detected
    #preprocessing
    img=imutils.resize(img,width=500)#resizing frames to width
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)#converting to gray scale img
    blur=cv2.GaussianBlur(grayimg,(21,21),0)#converting into blur image
    
    #save the first frame into fristframe variable
    #after 1st iteration it will not come into this if loop
    if firstframe is None:
        firstframe=blur
        continue
    
    imgdiff=cv2.absdiff(firstframe,blur)#diff between firstframe with current frame 
    threshimg=cv2.threshold(imgdiff,25,255,cv2.THRESH_BINARY)[1]#detected region will be converted to binary
    threshimg=cv2.dilate(threshimg,None,iterations=2)#by this we are going to remove some leftovers
    
    cnts=cv2.findContours(threshimg.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #we are going to find the outersurface by using findcontours(of img,its going to combine all pixels of detected obj,forming a chain to it)
    cnts=imutils.grab_contours(cnts)#reading cnts
    
    for c in cnts:
        if cv2.contourArea(c)< area:#if the contour value is lesser then only it detects else it will not
            continue
        (x,y,w,h)=cv2.boundingRect(c)
        #rectangle box function
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        #to gain rectangle(img/src,starting point,endpoint/height-width,color,thickness of rectangle)
        text="Moving Object detected"
        
    print(text)
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2)
    #displayingtext(img,text,(position on top left corner),font,font size,font color,font thickness)
    cv2.imshow("cameraFeed",img)#display the image of detecting objeect
    key=cv2.waitKey(1) & 0xFF
    if key==ord("q"):
        break
    
cam.release()
cv2.destroyAllWindows()