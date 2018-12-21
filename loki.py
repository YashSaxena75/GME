#Use of tuples
lokik=()
print("Hey hero,Welcome u have to ruin the world of monsters yey yey yey go go go go")
if not lokik:
    print("You are empty my hero")
    print("Don't worry princes has left some things in the way let me find out for you")
lokik=("Sword","Healing Potion","Dagger","playing cards")
for i in lokik:
    print("You have:",i)
print("You can play cards with the monster to pass the time")
input("Press Enter to continue")
print()
print("Hey you just found a chest")
chest=("Apple","Mango","Mobile")
print("Now ur inventory contains:")
lokik=lokik+chest
for j in lokik:
  print(j)
input("Press Enter to loose the game hero becuase you have got a mobile where u will play a game in which u will defeat the monster but in real life the monster will kill u")