c=None
x=""
print("This python scripts is a kind of small dictionary which tells u meaning of different hindi words in message kanguage")
print("Especially made for my beloved Indians!!!")
print("Special features in this dictionary are:")
print("""  

           0:Search the meaning of a word
           1:Add a new Hindi word
           2:Delete the word if it is wrong
           3:Update the meaning of the word
                                              """)


hind={"goli":"kisi ko bina bataye kahi chale jana.is shabd ka istemal kashipur me kiya jata hai",
      "chotu":"chai ki dukaan pr kaam karne wala jiski umar 14 se kam hai",
      "engineer":"ye sirf ek engineer he bata payga"}
print("Currently dictionary contains:",list(hind))
while c!=4:
 print("0:Search the word")
 print("1:Add a new Hindi word")
 print("2:Delete the word in case it is wrong")
 print("3:Update the meaning of the word")
 print("4:Exit")
 c=int(input("Please enter ur choice:"))
 if c==0:
  y=input("Enter a word to search its meaning:")
  if y in hind:
   print("Meaning of the word:",y)
   print(hind[y])
  else:
   print("Sorry mujhe iska mtlb nahi pata")
 elif c==1:
  z=input("Enter the word you want to add:")
  u=input("Enter the definition the word:")
  hind[z]=u
  print("Term is added succesfully!!!")
 elif c==2:
  t=input("Enter the word u want to delete from the dictionary:")
  del hind[t]
  print("Word is removed successfully!!!")
 elif c==3:
  z=input("Enter the word u want to define:")
  if z in hind:
   u=input("Enter the new definition:")
   hind[z]=u
   print("New definition edit!!!")
  else:
   print("This word doesn't exist in this dictionary")
 elif c==4:
  print("GOOD_BY!!!Leave a reply on cyberbot1502@gmail.com")

  

