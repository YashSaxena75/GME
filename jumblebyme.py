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
else:
 print("You loose the game")
input("Press Enter to exit")
