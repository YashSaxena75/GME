import time
import sys
import random
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
print(Base.WARNING+"██|"+Base.END,end="")
sys.stdout.flush()
time.sleep(0.3)
print(Base.WARNING+"██|"+Base.END,end="")
sys.stdout.flush()
time.sleep(0.3)
print(Base.WARNING+"██|"+Base.END,end="")
sys.stdout.flush()
time.sleep(0.3)
print(Base.WARNING+"██|"+Base.END,end="")
sys.stdout.flush()
time.sleep(0.3)
print(Base.WARNING+"██|"+Base.END,end="")
sys.stdout.flush()
time.sleep(0.3)
print(Base.WARNING+"██"+Base.END,end="")
sys.stdout.flush()
print("|")
time.sleep(0.3)


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

class Deck(Hand):
    def pop(self):
        for rank in Card.ranks:
            for suit in Card.suits:
                self.addcards(Card(rank,suit))

    def shuff(self):
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                 top_card = self.cards[0]
                 self.give(top_card, hand)
                else:
                 print("Can't continue deal. Out of cards!")


d=Deck()
print("Creating a new deck..")
print("Deck:")
print(d)
d.pop()
print("Now Deck contains all the 52 cards but after shuffling the cards are:")
d.shuff()
print(d)
hands=[hand,oh]

d.deal(hands,per_hand=5)
print("after adding 5 cards to per hand u both have:")
print("My hand have:")
print(hand)
print("Ur hand:")
print(oh)

d.clear()
print("\nDack is cleared now")
print(d)

class Unprintable_Card(Card):
    def __str__(self):
        return "<unprintable>"

class Positionable_Card(Card):
       def __init__(self, rank, suit, face_up=True):
            super(Positionable_Card, self).__init__(rank, suit)
            self.is_face_up = face_up

       def __str__(self):
           if self.is_face_up:
               rep = super(Positionable_Card, self).__str__() #This statement calls the Super lcass constructor
           else:#the first line " tells the python to call the super const. of the class Positionable_card
               rep = "XX"
           return rep

       def flip(self):
        self.is_face_up = not self.is_face_up


card1 = Card("A", "c")
card2 = Unprintable_Card("A", "d")
card3 = Positionable_Card("A", "h")
print("Printing a Card object:")
print(card1)
print("\nPrinting an Unprintable_Card object:")
print(card2)
print("\nPrinting a Positionable_Card object:")
print(card3)
print("Flipping the Positionable_Card object.")
card3.flip()
print("Printing the Positionable_Card object:")
print(card3)
input("\n\nPress the enter key to exit.")
