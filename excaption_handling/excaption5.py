class UserDefinedException(Exception):
    def __init__(self,s):
        print("Exception Caught:",s)

eng,math,sci=map(int,input("Enter marks: ").split())
try:
    if eng<0 or math<0 or sci<0:
        raise UserDefinedException("Error in marks")
except UserDefinedException as E :
    print(E)
else:
    print(eng,math,sci)
finally:
    pass