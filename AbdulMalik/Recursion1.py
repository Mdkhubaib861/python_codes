def fact(i):
    if i==1:
        return 1
    else:
        f=i*fact(i-1)
    return f

print(fact(int(input("Enter a Number: "))))