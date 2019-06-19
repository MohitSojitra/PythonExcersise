

class Employee:
    def __init__(self, name, id):
         self.name = name
         self.id = id
    
    def show_detail(self):
        print(f"name is {self.name} and id is {self.id}")
    
    @classmethod
    def get_detail(cls, info):
        return cls(*info.split(","))
    
    @staticmethod
    def print_compney():
        print("it is a j.s.m compney");

mohit = Employee("mohit" , 58)

raj = Employee.get_detail("raj , 90")
mohit.print_compney()
mohit.show_detail()
raj.print_compney()
raj.show_detail()

