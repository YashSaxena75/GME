import sys
import re
#import os
import time
w="So u wish to continue...."
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

c=''
#r=None
#d=None
while c!='\q':
 r=None
 d=None
 print("\n")
 f=input("Enter ur first number here:")
 if f==re.sub('[a-zA-Z,.:@()" "!#$^&=?<>{}`~;:]','',f):
  print("Number is correct....")
  r=1
 else:
  print(color.FAIL+"Error...."+color.END)
 
 s=input("Enter the second number here:")
 if s==re.sub('[a-zA-Z,.:@()" "!#$^&=?<>{}`~;:]','',s):
  print("Number is correct...")
  d=1
 else:
  print(color.FAIL+"Error...."+color.END)
 if r==1 and d==1: 
   print(color.OKGREEN+"                          ---------MENU---------"+color.END)
   print("""                                    
                            1.Addition
                            2.Subtraction
                            3.Divison
                            4.Multiplication          """)
 
   ch=int(input("Enter ur choice here:"))
   if ch==1:
    print("Addition of two numbers is:",float(f)+float(s))
   elif ch==2:
    print("Difference of two numbers is:",float(f)-float(s))
   elif ch==3:
    try:
     print("Division of two numbers is:",float(f)/float(s))
    except:
     print(color.FAIL+"Divide by zero Error..."+color.END)
   elif ch==4:
    print("Multiplication of two numbers is:",float(f)*float(s))
   c=input("want to perfrom some more calculations then enter c and if not then enter \q here:")
   if c=='c':
    for t in w:
     sys.stdout.write(t)
     sys.stdout.flush()
     time.sleep(0.05)
   else:
    print("Thanks for using me!")
 
 else:
  c="\q"
  print("GOOD-BYE!")
 
