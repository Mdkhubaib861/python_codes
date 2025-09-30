'''
Read marks in 6 subjects of a student
If the marks are illegal display invalid marks
else check if the student is pass or fail

marks1=int(input("Enter marks1: "))
marks2=int(input("Enter marks2: "))
marks3=int(input("Enter marks3: "))
marks4=int(input("Enter marks4: "))
marks5=int(input("Enter marks5: "))
marks6=int(input("Enter marks6: "))
if marks1>100 or marks2>100 or marks3>100 or marks4>100 or marks5>100 or marks6>100:
    print("Illegal Marks input")
else:
    if marks1<35 or marks2<35 or marks3<35 or marks4<35 or marks5<35 or marks6<35:
        print("Fail")
    else:
        print("Pass")
'''
marks = list(map(int, input("Enter marks: ").split()))
if len(marks) != 6:
    print("Invalid number of subjects: ")
else:
    if marks[0] > 100 or marks[1] > 100 or marks[2] > 100 or marks[3] > 100 or marks[4] > 100 or marks[5] > 100:
        print("Illegal Marks")
    else:
        if marks[0] < 35 or marks[1] < 35 or marks[2] < 35 or marks[3] < 35 or marks[4] < 35 or marks[5] < 35:
            print("Fail")
        else:
            if sum(marks) >= 400:
                print("Very Good: ", sum(marks))
            else:
                print("Good: ", sum(marks))