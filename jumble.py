import random
jumble=""
print("Hey this is a game in this game you have to guess what is the corrcect spelling of the jumble word")
print("Some of the words can be missed during the jumble you have to guess the words")
print("A word can contain min of 3 words and maximum of 5 words")
words=("Hey","Kali","Linux")
word=random.choice(words)
correct=word
pos=random.randrange(len(correct))
while word:
 jumble+=correct[pos]
 word = word[:pos] + word[(pos + 1):]
 print(word)
 break
#input("Press enter to exit")
x=input("enter ur word to guess the correct option")
if x==correct:
 print("You win the game")
else :
 print("You loose the game")
input("Press enter to exit")
