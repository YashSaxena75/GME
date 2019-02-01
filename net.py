import re
class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[93m'
    WARNING = '\033[92m'
    FAIL = '\033[91m'
    # Formatting
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    # End colored text
    END = '\033[0m' 
h_name=""

#from termcolor import colored, cprint
import socket
from binascii import hexlify
def mac():
 h_name=input("Enter the machine u want to search for:")
 try:
  print(color.OKBLUE+"IP address of "+h_name+":"+socket.gethostbyname(h_name)+color.END)
 except:
  print("Please Check ur internet connection...")


def conv():
 for h in ['127.0.0.1','192.168.43.248']:
  packed=socket.inet_aton(h)
  #print(h)
  upacked=socket.inet_ntoa(packed)

 print("IP address:")
 print("Unpacked====>",upacked)
 print("Packed====>",end="")
 print(hexlify(packed)) 

def port():
 prot='tcp'
 p=input("Enter the port number here in tcp:")
 if p==re.sub('[a-zA-Z,.:@()" "!#$^&=?<>{}`~;:]','',p):
  try:
   print(socket.getservbyport(int(p),prot))
  except:
   print(color.FAIL+"No such port exists..."+color.END)
 else:
  print(color.FAIL+"Wrong input...."+color.END)

# r=int(input("Enter the port number here in udp:"))
# print(socket.getservbyport(r,prots))

if __name__=='__main__':
 mac()
 conv()
 port()
