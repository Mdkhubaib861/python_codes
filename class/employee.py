class Employee:
    def __init__(self, empid, pname, dept, exp, basic):
        self.empid = empid
        self.pname = pname
        self.dept = dept
        self.exp = exp
        self.basic = basic
        self.allowances = 0
        self.annual = 0
        self.tax = 0
        self.gross = 0
    def cal_salary(self):

        if self.exp >= 10:
            self.allowances = self.basic * 0.30
        elif self.exp >= 5:
            self.allowances = self.basic * 0.20
        else:
            self.allowances = self.basic * 0.10
        self.annual = (self.basic + self.allowances) * 12
        if self.annual > 100000:
            self.tax = self.annual * 0.20
        elif self.annual > 50000:
            self.tax = self.annual * 0.10
        else:
            self.tax = self.annual * 0.05
        self.gross = self.annual - self.tax
    def display(self):
        print("Employee ID:", self.empid)
        print("Employee Name:", self.pname)
        print("Department:", self.dept)
        print("Experience (Years):", self.exp)
        print("Basic Salary:", self.basic)
        print("Allowances:", self.allowances)
        print("Annual Salary:", self.annual)
        print("Tax:", self.tax)
        print("Gross Salary:", self.gross)
e1 = Employee(101, "John Doe", "Finance", 6, 5000)
e1.cal_salary()
e1.display()


