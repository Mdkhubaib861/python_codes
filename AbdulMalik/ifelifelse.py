'''
emp=dict()
id=int(input("Enter employee id:"))
ename=input("Enter employee name:")
basic=float(input("Enter employee basic salary:"))
gross=basic*12
if gross>=1200000:
    tax=0.1*gross
elif gross>=1000000:
    tax=0.08*gross
elif gross>=800000:
    tax=0.06*gross
elif gross>=600000:
    tax=0.04
else:
    tax=0.02
net=gross-tax
emp["id"]=id
emp["name"]=ename
emp["basic"]=basic
emp["gross"]=gross
emp["tax"]=tax
emp["net"]=net
print(emp)

read roll, name and marks in 6 subjects of a student
and store them into a dictionary student
calculate total, percent and grade
marks=[85,77,88,99,55,62]
total/len(marks)
student={roll:5, name:Faiz,marks:[85,77,88,99,55,62],total:85, percent:78,grade:"A grade"}
with criteria
if percent>=75
 A grade
if percent>=60
 B grade
if percent>=50
 C grade
else
 D Grade

student=dict()
print(type(student))
name=(input("Enter student name: "))
rollno=int(input("Enter student rollno: "))
marks=list(map(int,input("Enter student marks: ").split()))
total=sum(marks)
percent=total/6
if percent>=75:
    print("A")
elif percent>=60:
    print("B")
elif percent>=50:
    print("C")
elif percent>=40:
    print("D")
elif percent>=30:
    print("E")
else:
    print("Fail")
student["name"]=name
student["rollno"]=rollno
student["marks"]=marks
student["total"]=total
student["percent"]=percent
print(student)
'''