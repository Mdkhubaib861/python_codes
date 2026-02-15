from logging import exception

try:
    n=int(input("Enter a number: "))
except ValueError as v:
    print("Error Caught:",v)
else:
    print(n**2)
finally:
    print("Now the program will move ahead")
