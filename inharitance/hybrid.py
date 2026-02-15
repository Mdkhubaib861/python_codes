# Hybrid Inheritance 

class Employee:
    def __init__(self, eid, ename, education):
        self.eid = eid
        self.ename = ename
        self.education = education

class Developer(Employee):
    def __init__(self, eid, ename, education, project):
        super().__init__(eid, ename, education)
        self.project = project

class Webdeveloper(Developer):
    def __init__(self, eid, ename, education, project, team):
        super().__init__(eid, ename, education, project)
        self.team = team

class AppDeveloper(Developer):
    def __init__(self, eid, ename, education, project, platform):
        super().__init__(eid, ename, education, project)
        self.platform = platform

    def AppDeveloperProfile(self):
       
        print(self.eid, self.ename, self.education, self.project, self.platform, sep="\n")

class DataScientist(Developer):
    def __init__(self, eid, ename, education, project, platform, skills):
        super().__init__(eid, ename, education, project)
        self.platform = platform
        self.skills = skills

    def DataScientistProfile(self):
        
        print(self.eid, self.ename, self.education, self.project, self.platform, self.skills, sep="\n")

class MERN(Webdeveloper):
    def __init__(self, eid, ename, education, project, team, skills):
        super().__init__(eid, ename, education, project, team)
        self.skills = skills

    def displayProfile(self):
        
        print(self.eid, self.ename, self.education, self.project, self.team, self.skills, sep="\n")

class MEAN(Webdeveloper):
    def __init__(self, eid, ename, education, project, team, skills):
        super().__init__(eid, ename, education, project, team)
        self.skills = skills

    def displayProfile(self):
        print(self.eid, self.ename, self.education, self.project, self.team, self.skills, sep="\n")


M1 = MERN(111, "Marco", "TY (Computers)", "Online Learning System", "Gold", "React.js")
M1.displayProfile()
print("_______________________________________________")
M2 = MEAN(222, "Alta", "TY (Computers)", "E-Commerce Platform", "Gold", "MongoDB")
M2.displayProfile()
print("_______________________________________________")
A = AppDeveloper(333, "Marco", "BE", "E-Commerce", "Android")
A.AppDeveloperProfile()
print("_______________________________________________")
DS = DataScientist(444, "saad", "sy(computer)", "AI Analytics", "Python", "Pandas")
DS.DataScientistProfile()
