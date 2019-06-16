import cv2
import numpy as np
import os,pyttsx3,shutil
from os.path import isfile,join
hiddenmodule=['cv2','pyttsx3','os','numpy']
engine=pyttsx3.init()
voices=engine.getProperty('voices')
rate = engine.setProperty('rate',170)   # getting details of current speaking rate
engine.setProperty('voice',voices[1].id)
volume = engine.setProperty('volume',10.0)   #getting to know current volume level (min=0 and max=1)
os.mkdir('C:/photo')
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
face_c=cv2.CascadeClassifier('face.xml')

def face_ex(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_c.detectMultiScale(gray,1.3,5)
    if faces is():
        return None
    for(x,y,w,h) in faces:
        cro_faces=img[x:x+w ,y:y+h]

    return cro_faces


cap=cv2.VideoCapture(0)
c=0
while True:
    ret,frame=cap.read()
    if face_ex(frame) is not None:
        c=c+1
        face=cv2.resize(face_ex(frame),(200,200))
        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
        f_path='C:/photo/'+str(c)+'.jpg'
        cv2.imwrite(f_path,face)
        cv2.putText(face,str(c),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

        cv2.imshow('Face cropper',face)
    else:
        print('Face not found!')

    if cv2.waitKey(1)==13 or c==100:
        break

cap.release()
cv2.destroyAllWindows()
print('Capturing your pics completed')
#Training the Model
data_path='C:/photo/'
onlyfiles=[f for f in os.listdir(data_path) if isfile(join(data_path,f))]

t_data,labels=[],[]

for i,files in enumerate(onlyfiles):
    image_path=data_path+onlyfiles[i]
    images=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    t_data.append(np.asarray(images,dtype=np.uint8))
    labels.append(i)
labels=np.asarray(labels,dtype=np.int32)

model=cv2.face.LBPHFaceRecognizer_create()
model.train(np.asarray(t_data),np.asarray(labels))
print("Trainig Completed")

face_c=cv2.CascadeClassifier('face.xml')

def face_det(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_c.detectMultiScale(gray,1.3,5)

    if faces is():
        return img,[]

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),1)
        faced=img[y:y+h,x:x+w]
        faced=cv2.resize(faced,(200,200))

    return img,faced
i=0
j=0
cap=cv2.VideoCapture(0)
while i<=135:
    ret,frame=cap.read()

    img,face=face_det(frame)

    try:
        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
        result=model.predict(face)
        print(result[1])
        if result[1]<500:
            confi=int(100*(1-result[1]/300))
            st=str(confi)+"% confidence"
        cv2.putText(img,st,(100,120),cv2.FONT_HERSHEY_COMPLEX,1,(250,120,255))

        if confi>75:
            cv2.putText(img, "Unlocked,Yash Saxena", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
            cv2.imshow('Made by Yash Saxena',img)
            j=j+1

        else:
            cv2.putText(img, "locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0,255))
            cv2.imshow('Made by Yash Saxena', img)
            j=0
    except:

        cv2.putText(img, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0))
        cv2.putText(img, "locked", (250, 250), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255))
        cv2.imshow('Made by Yash Saxena', img)
        pass

    if cv2.waitKey(1)==13:
        break
    i=i+1


cap.release()
cv2.destroyAllWindows()
shutil.rmtree('C:/photo')
