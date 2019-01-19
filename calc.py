import re
print("Welcome to my magical calculator")
print("--------------------Instructions-------------------")
print("""
                              1.Type '\q' to exit anytime    
                              2.ur equation must look like(a+b) 
                              3.you can do as many calculations as u want                         """)
run=True
prev=0
def hell():
     global run
     global prev
     eq=""
     if prev==0:
      eq=input("Enter Your equation here:")
     else:
          print(">>>",end=" ")
          eq=input(str(prev))
          print(" ")
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
                print("Divide by zero error")
          else:
            try:
             prev=eval(str(prev)+eq)
            except:
             print("Divide by zero error")

while run:
     hell()
