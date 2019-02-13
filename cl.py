from socket import *

host=''
port=44444
size=1024
addr=(host,port)
while True:
 tcp=socket(AF_INET,SOCK_STREAM)
 tcp.connect(addr)
 data=raw_input(">")
 if not data:
  break
 tcp.send("%s\r\n" % data)
 data=tcp.recv(size)
 if not data:
  break
 print "Message was:"
 print data.strip()
 tcp.close()

