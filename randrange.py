import random
z = "yes"
while z=="yes" or z=="y":
    z = input("do you want to roll a die(yes/no or y/n) :")
    if z=="yes" or z=="y":
        print(random.randrange(1,7,1))
    elif z=="no" or z=="n":
        print("thanku")
    else:
        print("enter a valid answer")
        z=input()
print("thanku")