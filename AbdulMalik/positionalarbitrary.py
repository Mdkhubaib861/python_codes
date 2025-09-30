def student(roll,name,*marks):
    print(roll,name,(sum(marks)/len(marks)),sep="\n")

student(1,"Maaz",84,96,74)
student(2,"Kashif",84,96,74,61)
student(3,"Faiz",84,54,96,12,74)