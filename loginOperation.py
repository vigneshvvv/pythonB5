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

userName = input("Enter your userName: ")
password = input("Enter your password: ")
loginStatus = False

for user in loginUsers:
    if(user["userName"] == userName and user["password"] == password):
        loginStatus = True
        break


if(loginStatus):
    print("Login successfull")
else: 
    print("Either userName or password incorrect")
