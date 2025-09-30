import os

# os.mkdir("Practice")
# print(os.getcwd())
os.chdir("Practice")
# print(os.getcwd())
'''
with open("Student.txt","w") as file1:
    for i in range(5):
        r=int(input("Enter roll no: "))
        n=input("Enter student name: ")
        m1,m2,m3=map(int,input("Enter 3 subject's marks: ").split())
        t=m1+m2+m3
        file1.write(f"{r} {n} {t}\n")
    file1.close()

with open("Student.txt","a") as file1:
    for i in range(5):
        r = int(input("Enter roll no: "))
        n = input("Enter student name: ")
        m1, m2, m3 = map(int, input("Enter 3 subject's marks: ").split())
        t = m1 + m2 + m3
        file1.write(f"{r} {n} {t}\n")
    file1.close()

with open("Student.txt","r") as file1:
    print(file1.read())
    file1.close()

f1="Student.txt"
f2="Backup.txt"
os.system(f"copy {f1} {f2}")

os.remove("Student.txt")

os.rename("Backup.txt","NewStudents")
'''