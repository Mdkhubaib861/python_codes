class NullInput(Exception):
    pass

class InvalidUser(Exception):
    pass

class Register:
    def __init__(self):
        self.email=""
        self.password=""
        self.user=""
        self.verifypass=""
        self.mobile=""

    def RegisterNow(self):
        try:
            self.user=input("Enter username: ")
            self.email = input("Enter email: ")
            self.password = input("Enter password: ")
            self.verifypass = input("Enter verify password: ")
            self.mobile = input("Enter Mobile: ")
            if self.user=="" or self.email=="" or self.password=="" or self.verifypass=="" or self.mobile=="":
                raise NullInput("Null Input")
            if len(self.user)<10 or len(self.user)>15:
                raise InvalidUser("Invalid User name")
        except NullInput as N:
            print(N)
        except InvalidUser as Iu:
            print(Iu)

R1=Register()
R1.RegisterNow()
