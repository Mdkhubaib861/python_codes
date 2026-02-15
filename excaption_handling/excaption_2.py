try:
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    x=input("Enter a character:")
   # c=x+a/b
    c=a/b
except ValueError as v:
    print("Error:",v)
except ZeroDivisionError as z:
    print("Error:",z)
except TypeError as t:
    print("Error:",t)
else:
    print(a,b,c,x)
finally:
    pass
