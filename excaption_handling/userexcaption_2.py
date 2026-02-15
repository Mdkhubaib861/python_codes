#comm
class NullInput(Exception):
    pass

class InvalidUser(Exception): 
    pass

class InvalidEmail(Exception):
    pass

class WeakPassword(Exception):
    pass

class PasswordMisMatch(Exception):
    pass

class InvalidMobile(Exception):
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
            if "@" not in self.email:
                raise InvalidEmail("Invalid Email, Please Enter Valid Email")
            if len(self.password)<5 or len(self.password)>10:
                raise WeakPassword("Please Enter Strong Password")
            if self.password != self.verifypass:
                raise PasswordMisMatch("Invalid Password")
            if not (self.mobile.isdigit() and len(self.mobile) == 10):
                raise InvalidMobile("Invalid Mobile Number")
        except NullInput as N:
            print(N)
        except InvalidUser as Iu:
            print(Iu)
        except InvalidEmail as Ie:
            print(Ie)
        except WeakPassword as Wp:
            print(Wp)
        except PasswordMisMatch as Pm:
            print(Pm)
        except InvalidMobile as Im:
            print(Im)

R1=Register()
R1.RegisterNow()


