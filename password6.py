username = []
usernamepassword = []
website = []
password = []

passwordcon = 1
accountsetupconfirm = 1
entryloop = 1
user = ""
total = 0
u = 0
l = 0
s = 0


def new():
    global u
    global l
    global s
    print("Condtions for using this software are as follows\nYou must be over the age of 13\n")
    age = int(input("Please Insert your age (Decimals will not be accepted): "))
    if age > 13:
     while accountsetupconfirm >= 1:
        name = input("Please Insert your First & Last Name: ")
        print(name)
        username = input("Please insert a Username: ")
        print(username)
        while passwordcon >= 1:
            passwordtry1 = input("Please Insert your new account password:  ")
            passwordtry2 = input("Please retype your last password: ")
        if passwordtry1 == passwordtry2:
            passwordcon + 1
        else: print("Please reconfirm your password")
        if len(password) >= 8:
            for i in password:
                if i.islower():
                    l = 1
                if i.isupper():
                    u = 1
                if i == "!" or i == "@" or i == "#" or i == "$":
                    s = 1
        total = u + s + l
        if total == 3:
            confirm = input("Please confirm that these details above are the details your are about to confirm")



def startmenu():
    print("Welcome to your Password Manager")
    print("Are you a new or exisiting user?")
    while entryloop >= 1:
        user = input("New or Exisiting: ")
        if user == "New":
            entryloop + 1
            print("You will now be directed to setup an account for this software")
            new()
        else:
            print("Please enter a correct response")


startmenu()
