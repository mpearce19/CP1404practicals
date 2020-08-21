# Password check


MINIMUM_PASSWORD = 5


def main():
    """Get and print password using functions."""
    password = get_password(MINIMUM_PASSWORD)
    print_asterisks(password)


def get_password(minimum_password):
    """Get valid password"""
    password = input("Please input password: ")
    while len(password) < minimum_password:
        print("That password is not long enough")
        password = input("Please input password: ")
    return password


def print_asterisks(password):
    """Print the number of asterisks their are letters in the password"""
    for i in password:
        print("*", end="")


main()

