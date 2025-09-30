'''
2: Write a function to read email id and password of a person
if the email id and password matches with any of the predefined
email and password , the user gets access other wise user is restricted
'''

def login(email,password):
    user=[{"email":"die@gmail.com","password":"123456"},
          {"email":"def@gmail.com","password":"963456"},
          {"email":"abc@gmail.com","password":"876456"},
          {"email":"xyz@gmail.com","password":"123976"},
          {"email":"pqr@gmail.com","password":"129436"},]
    for a in user:
        if email==a["email"] and password==a["password"]:
            print("Access Granted")
            print("Login successfull")
            break
    else:
        print("Invalid email and password")

login("def@gmail.com","963456")