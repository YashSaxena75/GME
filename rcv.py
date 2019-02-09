#run this file first then run the file named 'msg.py' to send the message successfuly!
import socket
ip=""
port=8090
size=1024

try:
 s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 print("Socket created succesfully.")
except: 
 print("Error while creating socket!" )

s.bind(('',port))
#s.connect((ip,port))
s.listen(3)
print("Listening....")
while True:
 (connection,address)=s.accept()
 print("Connected with:",address  )
 data=connection.recv(size)
 if data:
  print("message is:",data)
 else:
  print("Nothing to recieve")
 #connection.sendall("Thanks for connecting")
