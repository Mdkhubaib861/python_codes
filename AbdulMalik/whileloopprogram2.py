'''
1: Read fruit names into a list and stop when user types "stop"
2: Convert a number into binary use %2 and //2 ad these numbers to a list
and reverse the list
3: Read marks of a student in 6 subjects and store the marks in a list

l=[]
while True:
    n = input("Enter fruit name: ")
    if n=="stop":
        break
    else:
        l.append(n)
print(l)


l=[]
while len(l)<6:
    marks=int(input("Enter marks: "))
    l.append(marks)
print(l)
'''
l=[]
n=int(input("Enter a number: "))
while n>0:
    a=n%2
    l.append(a)
    n=n//2
l.reverse()
print(l)