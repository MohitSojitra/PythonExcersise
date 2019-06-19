
class Employee:
    
    def __init__(self, name, id , fees):
         self.name = name
         self.id = id
         self.fees = fees
    
    def show_detail(self):
        return (f"name is {self.name} and id is {self.id} and fees is {self.fees}")
    
    @classmethod
    def get_detail(cls, info):
        return cls(*info.split(","))
    
    @staticmethod
    def print_compney():
        print("it is a j.s.m compney");
    
    def __pow__(self , other):
        return (self.fees ** other.fees)
    def __truediv__(self , other):
        return (self.fees / other.fees)
    def __add__(self , other):
        return (self.fees + other.fees)
    def __str__(self):
        return self.show_detail()

mohit = Employee("mohit", 32 , 800 )
parth = Employee("kano", 33 , 200 )

print(mohit**parth)

print(mohit/parth)
print(mohit + parth)
print(mohit)



