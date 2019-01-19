import re
import time
import os
print("Welcome to my magical calculator")
print("--------------------Instructions-------------------")
print("""
                              1.Type '\q' anytime to exit    
                              2.ur equation must look like(a+b) 
                              3.you can do as many calculations as u want   
                              4.Type R to reset the calculator                            """)
run=True
prev=0
def hell():
     global run
     global prev
     eq=""
     if prev==0:
      eq=input("Enter Your equation here:")
     else:
          print("Enter more numbers to perfrom more operartions or \q to exit:",end=" ")
          eq=input(str(prev))
          print(" ")
     if eq=='R':
          print("Reseting----->>>")
          time.sleep(2)
          print("\n"*35)
     if eq == '\q':
          print("Good-Bye")
          print("Made by humanoid_hater(Yash Saxena)")
          run = False
     else:
          eq=re.sub('[a-zA-Z,.:@()" "!#$^&=?<>{}`~;:]','',eq)
          if prev==0:
           try:
            prev=eval(eq)
            print("You have entered:",prev)
           except:
                print("I can't think upto infinity....give another try")
          else:
            try:
             prev=eval(str(prev)+eq)
            except:
             print("I can't think upto infinity....giver another try")


while run:
     hell()
