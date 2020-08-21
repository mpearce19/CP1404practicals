minimum_password = 5

password = input("Please input password: ")
while len(password) < minimum_password:
    print("That password is not long enough")
    password = input("Please input password: ")
for i in password:
    print("*", end="")