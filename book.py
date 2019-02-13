from SocketServer import(TCPServer as TCP,StreamRequestHandler as SRH)
from tqdm import tqdm
import time
import sys
c=0
from time import ctime
host=''
port=44444
addr=(host,port)

class MyRequestHandler(SRH):
 def handle(self):
  for i in tqdm(range(10000)):
   time.sleep(0.001)
  print "Connected from:",self.client_address
  self.wfile.write('[%s]%s' % (ctime(),self.rfile.readline()))

tcp=TCP(addr,MyRequestHandler)
print "Waiting for the connection" 
#for i in tqdm(range(10000)):
# time.sleep(0.00001)
if c==0:
 tcp.serve_forever()
 c+=1
else:
 print "Thanks for Connecting with me!"
 sys.exit()
