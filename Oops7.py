

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


class Student(Employee):

    def __init__(self, name , id , languages):
        self.name = name
        self.id = id
        self.languages = languages

    def print_details(self):
        return f"the student name is {self.name} and his id is {self.id} and he knows {self.languages} languages"


if __name__ == '__main__':

    mohit = Employee("mohit" , 58)

    # raj = Employee.get_detail("raj , 90")
    # mohit.print_compney()
    # mohit.show_detail()
    # raj.print_compney()
    # raj.show_detail()



    kanani = Student("parth", 21, {"python", "c++" , "sql" , "java"})
    kanani.show_detail();
    print(kanani.print_details())
