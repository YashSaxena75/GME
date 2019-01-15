c=None
k=None
y=""
z=""
x=None
print("You have 30 points in the very starting of the game")
print("Rules for the game are:")
print("""
    
 

                  1:If you choose any attribute u will loose 7.5 points
                  2:You can take back ur points from that attribute
                  3:You will loose the game if ur points become 0 or less than 0
                                                                                                 """)
p=30
flag=0
att={"Strength":"You will loose 7.5 points","health":"Yo will loose 7.5 points"}
print("Attribute list contains",list(att))
while c!=0:
 c=int(input("Enter 0 here to exit or Enter 1 to continue the script:"))
 if c==0:
  print("GOOD-BYE!!!")
  flag=1
 if flag==0:
  y=input("Please Choose ur Attribute:")
  if y=='Strength':
   p-=7.5
   print("NOw ur points are:",p)
  elif y=='health':
   p-=7.5
   print("ur points are:",p)
  print("Choosed the wrong attribute accedentaly No worry just enter the 9 and see the magic")
  x=int(input("Enter 9 here:"))
  if x==9:
   z=input("Enter the wrongly selected Attribute here:")
   if 'Strength' in y:
    if z=='Strength':
     p+=7.5
     print("YIPEEE!!! you got ur points back,Ur points are:",p,"but if u cheat u will loose more points according to the rules!!!")
    else:
     print("U are trying to cheat bro!!!","now if you continue u will loose more points")
   if 'health' in y:
    if z=='health':
     p+=7.5
     print("Yipee you got ur points back,""ur points are:",p,"but if u cheat u will loose more points according to the rules!!! ")
    else:
     print("U are trying to cheat bro","now if you continue u will loose more points")
  else:
   print("According to u,u have entered the correct attribute so proceeding further.....")
 if p<=0:
  print("As ur points are zero now so You loose the game!exiting the game")
  c=0
