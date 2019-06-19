


class Student:
    no_of_l = 30
    
    def __init__(self, name , roll):
        self.name = name
        self.roll = roll

    

    def print_name(self):
        return f"the name is {self.name} , role number is {self.roll} ans total number of leave is {self.no_of_l}"

    @classmethod
    def change_l(cls , leave):
        cls.no_of_l = leave;
    
    @classmethod
    def c_o(cls, string1):
        # manu = string1.split("-")
        # print(manu)
        return cls(*string1.split("-") )


# mohit = Student("mohit" ,58)


# print(mohit.print_name());


# rahul = Student("rahul" , 3)
# print(rahul.print_name())
# mohit.change_l(40)
# print(rahul.print_name())
# print(rahul.no_of_l)



mamu = Student.c_o("mohit-459")

print(mamu.name)

