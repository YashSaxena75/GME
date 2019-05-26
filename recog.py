from gtts import gTTS
import playsound
print("ACM DITU STUDENT CHAPTER SPEECH RECOGNITION SYSTEM")
print("\n\n\n\n\n")
import speech_recognition as sr 
text=None 
while text!='done':
 r = sr.Recognizer()
 with sr.Microphone() as source:
  print("Say something!")
  audio = r.listen(source)
  print("Say Again to confirm")
  ad=r.listen(source)


  try:
        text = r.recognize_google(audio)
        te=r.recognize_google(ad)
        #print("You said : {}".format(text))
  except:
        print("Sorry could not recognize your voice")
 if te==text:
   text=text.replace(' ','')
   f=open(r"/root/Desktop/ACM")
   for line in f:
    line.strip().split('/n')
    if text in line:
     print("Present!")
     h=open(r"/root/Desktop/Att","a")
     h.write('\n')
     h.write(text+" Present ")
 
     language='en'
     v = gTTS(text=te, lang=language, slow=False)
     v.save("/root/Desktop/nope.mp3") 
     playsound.playsound('/root/Desktop/nope.mp3', True)

 else:
  print("Wrong ID!")
