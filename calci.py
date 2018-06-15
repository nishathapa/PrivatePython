
#if user inputs y then repeat otherwise exit
t=input("Do want to perform any calculation : (y/n)")
while t == "y":
    q = input("choose an operation: add,subtract,multiply,divide")
    # print(q)
    print("first number:")
    a = int(input())
    print("second number:")
    b = int(input())
    if q == "add":
        print(a + b)
    elif q == "subtract":
        print(a - b)
    elif q == "multiply":
        print(a * b)
    else:
        print(a / b)
    t = input("Do want to perform any calculation : (y/n)")
print("thanks")

