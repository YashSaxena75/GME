print("""
      
      M       M   OOOOOO  N     N  EEEEEE  Y    Y  
      M  M  M M   O    O  N N   N  E         Y Y
      M   M   M   O    O  N   N N  EEEEE      Y 
      M       M   OOOOOO  N     N  EEEEEE    Y
      
      
      """)
print("Please Enter all the money expenditure")
car = input("Lamborghini Tune-Ups: ")
car = int(car)

rent = int(input("Manhattan Apartment: "))
jet = int(input("Private Jet Rental: "))
gifts = int(input("Gifts: "))
food = int(input("Dining Out: "))
staff = int(input("Staff (butlers, chef, driver, assistant): "))
guru = int(input("Personal Guru and Coach: ") )
games = int(input("Computer Games: "))
#instead of converting the string to int while taking input from the user you can convert them while doing addition too
total = car + rent + jet + gifts + food + staff + guru + games

print("\nGrand Total:", total)

input("\n\nPress the enter key to exit.")