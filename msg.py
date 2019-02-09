import socket
import sys
import time
ip=""
port=8090
size=1024
msg=""
try:
 s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 print("Created successfuly...")
except:
 print("error while creating socket")

s.connect(('',port))
#s.bind((ip,port))
try:
 msg=input("Enter ur message here to send:")
 print("Trying to send ur message...")
 time.sleep(5)
 print("Error while sending the message,retrying")
 time.sleep(5)
 s.send(msg.encode('ascii'))
 print("message sent successfully....")
except:
 print("Error while sending the message to:",ip,"Via the port:",port)
