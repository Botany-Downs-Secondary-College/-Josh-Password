username = ["wifi"]
usernamepassword = ["Noobie!23"]
god = []
website = ["Outlook"]
webpassword = ["oompaloompa!#%"]

passwordcon = 1
accountsetupconfirm = 1
entryloop = 1
user = ""
total = 0
u = 0
l = 0
s = 0
authentication = 0


def new():
    global u
    global l
    global s
    global passwordcon
    global accountsetupconfirm
    print("Condtions for using this software are as follows\nYou must be over the age of 13\n")
    age = int(input("Please Insert your age (Decimals will not be accepted): "))
    if age > 13:
        while accountsetupconfirm >= 1:
            name = input("Please Insert your First & Last Name: ")
            print(name)
            username1 = input("Please insert a Username: ")
            print(username1)
            while passwordcon >= 1:
                passwordtry1 = input("Please Insert your new account password:  ")
                passwordtry2 = input("Please retype your last password: ")
                if passwordtry1 in passwordtry2:
                    print("Talk to me Goose")
                    password = passwordtry1
                    break
            break
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
        print("Password is valid!")
        print("Please confirm that these details above are the details your are about to confirm\nBy using 'Yes' these "
              "details are correct and valid and will become your login details\nBy using 'No' these details will be "
              "wiped and you will restart the process")
        confirm = input("Yes or No: ")
        print(confirm)
        if confirm == "Yes":
            print("You will now be directed to the start menu")
            usernamepassword.append(passwordtry2)
            username.append(username1)
            # god.apppend(Dict = dict({"Username: ",username1,"Password: ",passwordtry2}))
            #for i in username:
             #   print(i)
            #for i in usernamepassword:
             #   print(i)
            startmenu()
        elif confirm == "No":
            print("You will now be redirected to begin the process again")
            new()


def existing():
    global authentication
    global webpassword
    global website
    # print(username)
    # print(usernamepassword)
    # print(god)
    getname = input("Hello there please enter your username\nUsername: ")
    if getname in username:
        passwordcheck = input("Please input the password: ")
    if passwordcheck in usernamepassword:
        print("Bingo!")
        print("Would you like to add a new password or retrive a new password?\nEnter 'New' to add a new "
              "password, Enter 'Retrive' to retrive a password")
    existingexec = input("Enter action: ")
    if existingexec == "Retrive":
        passwordselection = input("Please input name of 'Website' or 'Application': ")
        if passwordselection in website:
            print("Your password is",webpassword)
    elif existingexec == "New":
        websitenew = input("Please input the name of the Website or Application: ")
        webpasswordnew = input("Please input the password of the Website or Application: ")
        website.append(websitenew)
        webpassword.append(webpasswordnew)
        if websitenew in website:
            if webpasswordnew in webpassword:
                print("Your details have been set as\nWebsite or Application:",websitenew,"\nPassowrd:",webpasswordnew,"")


def startmenu():
    print("Welcome to your Password Manager")
    print("Are you a New or Existing user?")
    while entryloop >= 1:
        user = input("New or Existing: ")
        if user == "New":
            entryloop + 1
            print("You will now be directed to setup an account for this software")
            new()
        elif user == "Existing":
            print("You will now be redirected to the login page")
            existing()
        else:
            print("Please enter a correct response")


startmenu()
