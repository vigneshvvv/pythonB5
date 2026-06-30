loginUsers = [
    {
        "userName": "Vignesh",
        "password": "Vignesh"
    },
    {
        "userName": "Deva",
        "password": "Deva"
    },
    {
        "userName": "Abdul",
        "password": "Abdul"
    },
    {
        "userName": "Revanth",
        "password": "Revanth@123"
    }
]

count  = 1

while(count >= 1):
    if(count == 4):
        print("Login attempts reached. pls try again after sometime")
        break

    userName = input("Enter your userName: ")
    password = input("Enter your password: ")

    for user in loginUsers:
        if(user["userName"] == userName and user["password"] == password):
            print("login successfull")
            break
    print("Either username or password incorrect. Remaining attempts: ", 3-count)
    count += 1
