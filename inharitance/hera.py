# Hierarchical Inheritance
class Hospital:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def display(self):
        print(self.name)
        print(self.rating)

class Ortho(Hospital):
    def __init__(self, dean, name, rating):
        super().__init__(name, rating)
        self.dean = dean

    def display_ortho(self):
        self.display()
        print(self.dean)

class Dental(Hospital):
    def __init__(self, staff_count, name, rating):
        super().__init__(name, rating)
        self.staff_count = staff_count

    def display_dental(self):
        self.display()
        print(self.staff_count)

h1 = Hospital("Noor Hospital", 4.2)
h1.display()
print("......................................")

ortho_dep = Ortho("Dr.marco", "Noor Hospital", 4.2)
ortho_dep.display_ortho()
print("......................................")
dental_dep = Dental(15, "Noor Hospital", 4.2)
dental_dep.display_dental()
