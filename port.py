# usr/bin/python
# Here we are going to use Python Socket programming!

import socket
web=raw_input("Enter the website: ")
ip=socket.gethostbyname(web)
print "IP address of:", web ,"is :",ip
#port=input("Enter the port number: ")
for x in range(0,22):
	port=x
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	if sock.connect_ex((ip,port)):
		print "----------------------------"
		print "Port" , port ,"is closed!"
	else:
		print "----------------------------"
		print "Port" ,port ,"is open!"



