#Single Inheritance
class Vehicle:
    def __init__(self,type):
        self.type=type

    def dispType(self):
        print(self.type)

class Commercial(Vehicle):
    def __init__(self,type,brand,modal):
        super().__init__(type)
        self.brand=brand
        self.modal=modal

    def display(self):
        print(self.brand)
        print(self.modal)

C1=Commercial("Industrial","BMW","M4")
C1.dispType()
C1.display()



