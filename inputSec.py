operation = int(input("Enter a operation to perform 1. Addition 2. SUB 3.Multiplication 4.Division: " ))
a = int(input("Enter a number A: "))
b = int(input("Enter a Number B: "))

if(operation == 1):
    print(a+b)
elif(operation == 2):
    if(a >b):
        print(a-b)
    else:
        print("B is greater than A so result is in Negative", a-b)
elif(operation == 3):
    print(a*b)
elif(operation == 4):
    print(a/b)
else:
    print("Invalid Operation please choose correct one")