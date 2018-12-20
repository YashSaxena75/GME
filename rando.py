import random
print("Hey Dear,welcome to world of guessing the numbers")
print("What u need is just enter any number between 1-100")
print("And you have to guess what number will be given by me")
print("If you guess the right you win and and last i will tell u no. of tries")
print("So let me start the game")
c=0
x=int(input("Enter any number between 1-100"))
print("the computer is generating some random shit")
z=random.randint(1,x)
print(z)
print()
y=int(input("Please enter ur number to win this game"))
while y!=z:
  if y==z:
    print("I am here")
    c+=1
    print("No. of tries is:",c)
  elif y!=z:
     y = int(input("Enter ur guess again"))
     c += 1
     print("Tris:",c)
  #if y==z:
   #   print("Yipee!!!You win The game!!!")


input("Enter to exit")