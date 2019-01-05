#As in this game player has to guess only 1 word that's why there is no need to increase the score either it will be 1 or -1
import random
print("we are going to play a game so let us start the game in a second or may be in a couple of minutes")
print("So u have to guess the correct spelling of the word that is going to be display in ur screen")
words=("Linux","hey","there")
y=random.choice(words)
z=list(y)
c=random.sample(z,len(z))
print(c) 
print("The jumbled word is in front of u","Enter the correct guess to win the game")
a=input("Enter ur guess here:")
if a==y:
 print("You win the game")
 print("Your score is 1")
else:
 print("Having some difficulty in guessing the word","If yes then press 1,2,3 to show the hint but u have obly 1 chance to show the hint one of thse $
 s=int(input("Enter 1 or 2 or 3 to show the hint:"))
 if s==1:
  print("hint:Lin_x")
  print("Your score is -1")
 elif s==2:
  print("hint:h_y")
  print("Your score is -1")
 else:
  print("Hint:th_re")
  print("Your score is -1")
 print("Now u know the hint if u guess the right word ur score will be increased by 1")
 b=input("Enter ur guess again but this is the last time:")
 if b==y:
  print("You win the game")
  print("Final score after watching the hint is 0")
 else:
  print("you can't try any more!!!you loose the game")
  print("\a")
  print("\a")
  print("I think u have pressed the wrong number from 1,2,3 may be the number u have pressed doesn't contain the hint for ur word")
input("Press Enter to exit")
