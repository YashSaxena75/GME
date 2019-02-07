# type nc -l 5555 in ur terminal to check the connection

import socket
host='localhost'
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #This sock_stream indicates for the tcp
addr=(host,5555)
sock.connect(addr)
try:
    msg=b"This is a test\n"
    sock.sendall(msg)
except:
    print("Socket error")
finally:
    sock.close()

