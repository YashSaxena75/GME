#Hey hero is surrounded my many enemies
# let us play another game and let me know you his strength
print("""
      
       SSSSS       TTTTTTTT      A A A A      GGGGGGG    EEEEEEEE    1 
       S              T          A     A      G          E           1 
       S              T          A     A      G          E           1 
       SSSSS          T          A A A A      GGGGGGG    EEEEEEEE    1
           S          T          A     A            G    E           1
           S          T          A     A            G    E           1
       SSSSS          T          A     A            G    EEEEEEEE    1
      """)
power=10
trolls=0
damage=3
while power>0:
     trolls += 1
     power-=damage
     if power>0:
      print("Your hero poer is",power)
     if power<0:
         break


print("Defeated:",trolls-1)
input("Game Over!!!Press Enter to exit")
