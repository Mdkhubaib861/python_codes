'''
1: Create a directory in your current working directory with name as
'Documents'
2: Move inside the 'Documents'
3: Create two directories
'Personal'
'Academics'
4: List the contents of "Documents"
5: Delete the directory "Personal"
6: Move inside the "Academics" Direcotry
7: Create a file with name as "college.txt" and
write the name of your college and its lcoation in it
'''

import os
print(os.getcwd())
# os.mkdir("Documents")
os.chdir("Documents")
# os.mkdir("Personel")
# os.mkdir("Academics")
print(os.listdir())
# os.rmdir("Personel")
os.chdir("Academics")
print(os.getcwd())
with open("College.txt","w") as file1:
    file1.write("MMANTC, Malegaon")
    file1.close()

