#Use of list...
print("Hey let's us play the hero game with the help of lists this time if you haven't play our old games which is based on tupples go and play that first")
list=[]
a=0
if not list:
 print("Sorry you don't have anything in ur doraemon 3d pocket")
print("But don;t worry doraemon has left some of its gadgets while flying with the help of bamboo copter let me add those to ur 3d pocket")
list=["energy drink","shield","invisible drink","sword","sleeping pills","new shoes","dragon's brother","anywhere door"]
print("Now ur list contains the following items:")
for i in list:
 print(i)
print("Stage 1 completed>>>>")
p=int(input("Enter 2 to enter in the second stage"))
if p==2:
 print("Welcome to the second stage")
 print("There are total 3 trees in this stage go and search them for new items")
 print("""
            ---------   ---------   -----------
             -------     -------      -------
              -----       -----        ----- 
               ---         ---          ---
                |           |            |
                |           |            |
                |           |            |
                |           |            |                       """)
 t=int(input("Press 1 to search the first tree"))
 list1=[]
 if t==1:
  if not list1:
   print("This tree is too old to give some new items go ahead and search for the second one")
 t1=int(input("Enter 3 to search the second tree"))
 if t1==3:
   list2=["Potion","ShotGun","Sonio","Nobita Nobi","Car","Gyan goda","Shuzuka not found"]
   print("I think you have got something in this tree let me add these items to ur pocket")
   list+=list2
 print("Now you have:")
 for j in list:
  print(j)
else:
 print("You don't want to proceed I think so....")
 s=int(input("Enter 2 again to go to second stage this is the last time after this ur game will be terminated:"))
 if s==2:
  print("Welcome to the second stage")
  print("There are total 3 trees in this stage go and search them for new items")
  t=int(input("Press 1 to search the first tree"))
  list1=[]
  if t==1:
   if not list1:
    print("This tree is too old to give some new items go ahead and search for the second one")
  t1=int(input("Enter 3 to search the second tree"))
  if t1==3:
    list2=["Potion","ShotGun","Sonio","Nobita Nobi","Car","Gyan goda","Shuzuka not found"]
    print("I think you have got something in this tree let me add these items to ur pocket")
    list+=list2
  print("Now you have:")
  for j in list:
   print(j)
 else:
  input("Game over Press Enter to exit")
  a=1
if a==0:
 p1=int(input("Stage 2 completed press 5 to continue to stage 3...."))
 if p1==5:
  print("Welcome to the 3rd Stage....")
  print("Now you have dragon's brother go and try to save the queen by putting a gun on his head")
  print("""
              --------() ------
              ------()   |.  .|
               |         |    |
               |         ------
               |          |  |\ 
               |          |  | \
                          |  |  \
                           ---    \
                           _|_

                                               """) 

  print("Now u have put the gun on the dragon's brother head Now yell at call the dragon out to take ur queen back and return the dragon's brother...")
  print("it's victory time Yeahhhhhhh.............")
  print("Here comes the dragon")
  print("\a")
  print("""

                --------------
                |            |
                |   .   .    |
                |            |
                |   -----    |
                |            |
                |            |
                --------------
                 / |       |\
                /  |       | \
               /   |       |  \
              /    |       |   \
             /     |       |    \
            /      |       |     \
                   ---------
                      | |
                      | |
                      | |
                     _| |_


>>>LEAVE MY BROTHER OTHERWISE I WILL KILL THE QUEEN!!!!
>>>Shoot the dragon's brother and run towards the dragon
>>>HAHAHAHAHA!!! the dragon has burnt down ur sword now there is no more sword go and hide in the trees
>>>GO!GO!GO!GO!GO!

""")
  print("Stage 3 completed but you have lost ur sword now ur pocket contains:")
  del list[3]
  for r in list:
   print(r)
  print("According to ur eagle the dragon has killed the queen and doesn't live in this jungle go and and find him in next jungle..")

