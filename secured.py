#so this program uses many things we have studied so far
print("\nWelcome saar to our pisco security Network")
print("\nHope ur doing good saar!!!")
print("\nI need ur name and password to validate u")
name=input("\nPlease saar enter ur name here")
password=input("\nPlease enter ur password here")
security=0
print("\nSaar we have different security levels for different kind of peoples working in our organisation")
if name=="Josh" and password=="canada":
    print("\nWelcome Mr.",name)
    security=5
    print("\nu are most important to us saar")
elif name=="john" and password=="ui":
    print("\nThannks Mr.",name,"For your conribution")
    security=2
elif name=="Guest" and password=="Guest":
    print("\nThanks for using us")
    security=0
    print("\nYou are just a user man")
else:
    print("You are a third person You can't access the serve")
    print("Sounding the alarms")
    #why alarm doesn't sound 5 times?????
    print("\a"*5)

input("\nPlease press Enter to exit")