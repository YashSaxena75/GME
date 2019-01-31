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

import socket
c=None
cont=["www.google.com","www.bing.com","www.gmail.com","www.images.google.com"]
print("you can know the IP of the following machines")
for i in cont:
 print(i)

j=int(input("Enter the number for ur choice...first one starts from 0 index! Please enter ur choice here:"))
if j==0:
 h_name="www.google.com"
elif j==1:
 h_name="www.bing.com"
elif j==2:
 h_name="www.gmail.com"
else:
 h_name="www.images.google.com"
def mac():
 try:
  print(color.WARNING+"IP address of "+h_name+":"+socket.gethostbyname(h_name)+color.END)
 except:
  print("Please Check ur internet connection...")

if __name__=='__main__':
 mac()
