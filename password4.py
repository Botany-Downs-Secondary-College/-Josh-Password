website = []
password = []

y = 1
user = ""


def new():
    print("Condtions for using this software are as follows\nYou must be over the age of 13\n")
    age = int(input("Please Insert your age (Decimals will not be accepted): "))
    if age > 13:
        print("Yesyesyesy")

new()

print("Welcome to your Password Manager")
print("Are you a new or exisiting user?")
user = input("New or Exisiting: ")
while y >= 1:
    if user == "New":
        y + 1
        new()
    else:
        print("Please enter a correct response")
