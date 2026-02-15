class personal:
    def __init__(self,name,email,mobile,city):
        self.name=name
        self.email=email
        self.mobile=mobile
        self.city=city


class Academics:
    def __init__(self,degree,year,university,grade):
        self.degree=degree
        self.year=year
        self.university=university
        self.grade=grade
        

class Skills:
    def __init__(self,main_skill,sub_skill):
        self.main_skill=main_skill
        self.sub_skill=sub_skill


class Resume(personal,Academics,Skills):
    def __init__(self,title,main_skill,sub_skill,degree,year,university,grade,name,city,mobile,email):


        Skills.__init__(self,main_skill,sub_skill)
        Academics.__init__(self,degree,year,university,grade)
        personal.__init__(self,name,city,mobile,email)
        self.title=title

    def displayResume(self):
        print(self.title)
        print(self.main_skill)
        print(self.sub_skill)
        print(self.name)
        print(self.mobile)
        print(self.email)
        print(self.city)
        print(self.degree)
        print(self.university)
        print(self.year)
        print(self.grade)

R1=Resume("AI  ML engineer as a frasher","AI","ML","computer engineering",2025,"MIT university","A","marco","Malegaon",6465416465,"marco@gmail.com")
R1.displayResume()
