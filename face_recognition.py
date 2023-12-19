#LBP Recognition(linear binary pattern)

import cv2,os

haar_file='haarcascade_frontalface_default.xml'
datasets="datasets" #variable for the dataset
sub_data="sameed" #varaible for the particular persons datasets


#after this we should create path to the datasets
path=os.path.join(datasets, sub_data)#its combining the datsets and subdata
#checking weither its in path or not, if its not then 
#loading path to the directory
if not os.path.isdir(path):
    os.mkdir(path)
(width, height)=(130, 100)

face_cascade=cv2.CascadeClassifier(haar_file)#we loaded the haarcascade file
cam=cv2.VideoCapture(0)

count=1
while count<31:
    print(count)
    (_,im)=cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray, 1.3, 4)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
        face=gray[y:y+h,x:x+w]
        face_resize=cv2.resize(face,(width,height))
        cv2.imwrite('%s/%s.png'%(path,count),face_resize)
    count+=1
    
    cv2.imshow("opencv",im)
    key=cv2.waitKey(10)
    if key==27:
        break
     
cam.release()
cv2.destroyAllWindows()