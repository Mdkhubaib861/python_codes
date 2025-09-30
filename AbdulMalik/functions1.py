'''
def greetings(name,subject):
    print("Welcome")
    print("Mr.",name,"Subject",subject)

greetings("Mazz","c++")
greetings("Abdullah","python")
greetings(input("Enter name: "),input("Enter subject: "))


def list(l1, l2):
    if len(l1) != len(l2):
        print("Invalid Argument")
    else:
        total = 0
        for i in range(len(l1)):
            if l1[i] > l2[i]:
                total += l1[i]
            else:
                total += l2[i]
        print("sum of largest number =", total)

list([12, 32, 54, 74, 12], [63, 87, 62, 94, 12])

def list(l1, l2):
    total = 0
    if len(l1) != len(l2):
        print("Invalid Argument")
        return "Length not match!"
    else:
        for i,j in zip(l1,l2):
            if i>j:
                total+=i
            else:
                total+=j
        return "sum of largets number="+str(total)

print(list([12, 32, 54, 4, 12], [63, 87, 62, 9, 12]))


def operations(a,b):
    print("Basic operations:")
    return "add :"+str(a,b)
'''

def arithmetic(a, b):
    print("Basic Arithmetic operation: ")
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)

a = int(input("Enter the number for a: "))
b = int(input("Enter the number for b: "))

arithmetic(a, b)
