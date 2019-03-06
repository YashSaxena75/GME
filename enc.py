import progressbar
import sys
import time
from tqdm import tqdm

def bash():
 delay_print("Atbash encryption method ready to launch!")
 s=""
 print("\n")
 s=input("Enter ur message here to encrypt:")
 l=len(s)
 while l!=0:
  for t in s:
   if t=='a':
    y=97+25
    print(chr(y),end="")
    l=l-1
   elif t=='b':
    u=98+23
    print(chr(u),end="")
    l=l-1
   elif t=='c':
    u=99+21
    print(chr(u),end="")
    l=l-1
   elif t=='d':
    u=100+19
    print(chr(u),end="")
    l=l-1
   elif t=='e':
    u=101+17
    print(chr(u),end="")
    l=l-1


def delay_print(s):
 for c in s:
  print(c,end="")
  sys.stdout.flush()
  time.sleep(0.1)
 
def bar():
 progress = progressbar.ProgressBar()
 for i in progress(range(25)):
    time.sleep(0.4)


delay_print("This Script Can Encrypt Ur Message In a Different Manner So That No Other Third Person Can Read It!")
bar()
print("""
                  1.Atbash Encryption
                  2.Rot13
                  3.Rot22
                  4.Simple Encryption(add 1)
                  5.caesar(with ur key) 
 
                                              """)
c=0
c=int(input("Please Choose ur encryption Method from the following techniques listed above:"))
if c==1:
 bash()
