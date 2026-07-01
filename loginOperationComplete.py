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

count = 1

def login():
    global count
    while(count >=1):
        if(count == 4):
            print("maximum attempt reached")
            response = input("Do you want to reset your password?")
            if(response == "yes"):
                count = 1
                forgetPassword()
                break
            else:
                break
        userName = input("Enter your userName: ")
        password = input("Enter your password: ")

        loginStatus = False
        for user in loginUsers:
            if(user["userName"] == userName and user["password"] == password):
                loginStatus = True
                break
        if(loginStatus):
            print("login successfull")
            break
        else:
            print("Either userName or password incorrect. attempt remaining: ", 3-count)
            count += 1
        
def forgetPassword():
    userName = input("Enter your userName: ")
    password = input("Enter your password: ")
    reEnter = input("Re-Enter your password: ")

    if(password == reEnter):
        exist = False
        for user in loginUsers:
            if(user["userName"] == userName):
                exist = True
                user["password"] = password

        if(exist):
            print("Password reset successfull.. redirecting to login")
            login()
            exit
        else:
            print("User doesn't exist please register to continue.")

def registration():
    userName = input("Enter your userName: ")
    password = input("Enter your password: ")
    reEnter = input("Re-Enter your password: ")

    if(password == reEnter):
        user = {
            "userName": userName,
            "password": password
        }  
        loginUsers.append(user)
        print("redirecting to login...")
        login()
    else: 
        print("Password and re-entered password doesn't match. please try again")


response = int(input("Select operation to perform 1. login 2.Registration 3.ResetPassword"))
if(response == 1):
    login()
elif(response == 2):
    registration()
elif(response == 3):
    forgetPassword()
else:
    print("Invalid operation.")