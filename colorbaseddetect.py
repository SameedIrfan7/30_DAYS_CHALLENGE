import imutils #resizing library - import
import cv2 #opencv


redLower = (0, 100, 100)
redUpper = (10, 255, 255)
#giving the color to detect(hue,saturation,value)

cam=cv2.VideoCapture(0) #Camera init.

while True:

        (grabbed, frame)=cam.read() #reading frame from camera
        frame = imutils.resize(frame, width=600) #resizing the Frame
        blurred = cv2.GaussianBlur(frame, (11, 11), 0) #smoothing
        
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV) #convert bgr to hsv color format
        
        mask = cv2.inRange(hsv, redLower, redUpper) #mask the given color
        mask = cv2.erode(mask, None, iterations=2) #this is for shrink the white boundries
        mask = cv2.dilate(mask, None, iterations=2)#this is to fill the white boundaries

        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]#finding contours or surface of object
        center = None
        if len(cnts) > 0:
                c = max(cnts, key=cv2.contourArea) #accessing the area of object
                ((x, y), radius) = cv2.minEnclosingCircle(c) #froming circle fro that onject
                M = cv2.moments(c) #catching the moment
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))  #giving a small circle to define which is object
                if radius > 10:
                        cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2) # its shows outer circle for object
                        cv2.circle(frame, center, 5, (0, 0, 255), -1) #it shows red circle 
        
                        if radius > 250: #print(center,radius)
                                print("stop")
                        else:
                                if(center[0]<150):
                                        print("Left")
                                elif(center[0]>450):
                                        print("Right")
                                elif(radius<250):
                                        print("Forward")
                                else:
                                        print("Stop")
        cv2.imshow("Frame", frame) #displaying frames
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
                break

cam.release()
cv2.destroyAllWindows()
