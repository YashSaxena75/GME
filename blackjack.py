import time
class Base:
    # Foreground:
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
    NC ='\x1b[0m' # No Colo

print("Let us Play the BLackJack Game")
print("\n")
print("|",end="")
print(Base.WARNING+"███"+Base.END,end="")
print("|",end="")
time.sleep(0.8)
print(Base.WARNING+"███"+Base.END,end="")
print("|",end="")
time.sleep(0.8)
print(Base.WARNING+"███"+Base.END,end="")
print("|",end="")
time.sleep(0.8)
print(Base.WARNING+"███"+Base.END,end="")
print("|",end="")
time.sleep(0.8)
print(Base.WARNING+"███"+Base.END,end="")
print("|",end="")
time.sleep(0.8)
print(Base.WARNING+"███"+Base.END,end="")
print("|",end="")
time.sleep(0.8)
print(Base.WARNING+"███"+Base.END,end="")
print("|")
time.sleep(0.8)


print("\n")
class Card:
    ranks=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    suits=["c","d","h","s"]

    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit

    def __str__(self):
        rep=self.rank+self.suit
        return rep

class Hand:
    def __init__(self):
        self.cards=[]
    def __str__(self):
        if self.cards:
            rep=" "
            for card in self.cards:
                rep+=str(card)+" "
        else:
            rep="<Empty>"

        return rep

    def clear(self):
        self.cards=[]

    def addcards(self,card):
        self.cards.append(card)

    def give(self,card,ohand):
        self.cards.remove(card)
        ohand.addcards(card)

Cards=Card(rank="A",suit="c")
#print(Cards)
Card1=Card(rank="2",suit="c")
Card2=Card(rank="3",suit="c")
Card3=Card(rank="4",suit="c")
Card4=Card(rank="5",suit="c")

print("Initially the cards are:")
print("",Cards,"\n",Card1,"\n",Card2,"\n",Card3,"\n",Card4,"\n")


hand=Hand()

print("Currently my hand is:",hand,"/",hand,":",end=" ")
print(Base.WARNING+"||"+Base.END," ")


hand.addcards(Cards)
hand.addcards(Card1)
hand.addcards(Card2)
hand.addcards(Card3)
hand.addcards(Card4)
print("After Adding 5 cards from the above list i Have:",hand)
print("5/5",Base.OKGREEN+"|██████████|"+Base.END," ")


print("I am giving you my two cards:")

oh=Hand()
hand.give(Cards,oh)
hand.give(Card1,oh)

print("Now ur hand have:",oh)
print("2/2",Base.FAIL+"|█████████|"+Base.END)
print("\n")
print("My hand have:",hand)
print("3/5",Base.BOLD+"|███|"+Base.END)

print("Clearing my hand......")
hand.clear()
time.sleep(3)
print("Now I have:",hand)
print("0/5",Base.NC+"|█|"+Base.END)
print("Press Enter to exit")
