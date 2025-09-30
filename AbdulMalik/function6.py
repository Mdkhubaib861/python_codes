'''
Create an array of dictionaries which stores student data in following format
[{"roll":1,"Name":"Shaique","Gender":"Male","Percent":68.52},
{"roll":2,"Name":"Shaique","Gender":"Male","Percent":68.52}
{"roll":3,"Name":"Shaique","Gender":"Male","Percent":68.52}
{"roll":4,"Name":"Shaique","Gender":"Male","Percent":68.52}
]
Write a menu driven program with following options
1: Display Details of one student
2: Display Details of All Students
3: Display DEtails of All Male Students
4: Display Details  of All MAle students with percent>=75
'''
d = {
    1: {'name': 'Amit', 'gender': 'Male', 'percent': 80},
    2: {'name': 'Sara', 'gender': 'Female', 'percent': 85},
    3: {'name': 'Raj', 'gender': 'Male', 'percent': 70}
}

print("1: Single student data")
print("2: All student data")
print("3: All student data with Male")
print("4: All student data Male with percent > 75")

o = int(input("Enter an option: "))
if o == 1:
    student_id = int(input("Enter student ID: "))
    Display(d, "student_id")
elif o == 2:
    DisplayAll(d)
elif o == 3:
    DisplayMale(d, "Male")
elif o == 4:
    DisplayMale75(d, "Male", 75)
else:
    print("Invalid option")