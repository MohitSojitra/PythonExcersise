
class Student:
    no_of_l = 30
    
    def __init__(self, name , roll):
        self.name = name
        self.roll = roll

    

    def print_name(self):
        return f"the name is {self.name} , role number is {self.roll} ans total number of leave is {self.no_of_l}"



mohit = Student("mohit" ,58)


print(mohit.print_name());


rahul = Student("rahul" , 3)
print(rahul.print_name())