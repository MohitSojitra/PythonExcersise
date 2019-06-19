
class Student:
    no_of_l = 30



mohit = Student()
khajur = Student()


mohit.name = "mohit"
mohit.salary = 300000000000

khajur.name = "khajur"
khajur.salary = 40000

print(khajur.salary , khajur.no_of_l)

print(khajur.__dict__)

print(mohit.__dict__)
print(Student.__dict__)

mohit.no_of_l = 300


print(mohit.__dict__)
Student.no_of_l = 40

print(khajur.no_of_l)