import random
print("Hey there this app will tell u the no. of heads and tails")
print("Let us toss the coin 100 times")
n=100
print("There will be head or tail")
h=0
t=101
c=0
d=0
z=random.randint(1,100)
print(z)
print()
while z>0:
    if z>h and z<100:
     print("I am here")
     c+=1
     print("A head was occured with no. of times",c)
    elif z<t and z>100:
        d+=1
        print("A tail was occured with no.of times",d)


input("Enter")
