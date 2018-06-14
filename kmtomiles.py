q=input("choose the unit to be converted into miles : km/m/f")
print(q)
if q=="km":
    print("enter the distnace in km to be converted to miles : ")
    kim = int(input())
    print(kim*1.609,"miles")
elif q=="m":
    print("enter the distance in meters to be converted into miles : ")
    m = int(input())
    print(m*0.00062137,"miles")
elif q=="f":
    print("enter the distance in feet to be converted into miles : ")
    f = int(input())
    print(f*0.000189,"miles")
else:
    print("thanku")
