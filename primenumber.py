# Python program to check if the input number is prime or not

p=int(input())

if p>1:
    for i in range(2,p):
        if p%i==0:
            print(p,"not a prime number")
            break
    else:
        print(p,"is a prime")
else:
    print(p,"is a not a prime")
