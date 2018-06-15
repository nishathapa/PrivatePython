
q=input("choose an operation: add,subtract,multiply,divide")
print(q)
print("first number:")
a=int(input())
print("second number:")
b=int(input())
if q=="add" :
    print (a+b)
elif q=="subtract":
    print (a-b)
elif q=="m  ultiply":
    print (a*b)
else:
    print (a/b)
