website = []
password = []

y = 1
user = ""
total = 0


def new():
    print("Condtions for using this software are as follows\nYou must be over the age of 13\n")
    age = int(input("Please Insert your age (Decimals will not be accepted): "))
    if age > 13:
        name = input("Please Insert your First & Last Name: ")
        print(name)
        password = input("Please Insert your new Password ")
        if len(password) >= 8:
            for i in password:
                if password.islower():
                    l = 1
                if password.isupper():
                    u = 1
                if i == "!" or i == "@" or i == "#" or i == "$":
                    s = 1
        total = u + s + l
        if total == 3:
            print("goodie goodie")


def startmenu():
    print("Welcome to your Password Manager")
    print("Are you a new or exisiting user?")
    while y >= 1:
        user = input("New or Exisiting: ")
        if user == "New":
            y + 1
            new()
        else:
            print("Please enter a correct response")


startmenu()
