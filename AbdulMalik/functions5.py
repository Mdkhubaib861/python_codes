'''
1: Create a function to read fname and lastname from the
user and return the full name in Uppercase

'''


def uppercase():
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    full_name = f"{fname}{lname}".upper()
    return full_name

print("uppercase:", uppercase())
