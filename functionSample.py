def add(a ,b):
    # c= a+b
    # return c
    return a+b

def addNew(a,b,c):
    print(a+b+c)


result = add(100, 120)
if(result %2 == 0):
    print("Even number")
else:
    print("odd number")
add(200, 120)
add(300, 120)
addNew(120,230,430)