from abc import ABC , abstractmethod

class Person(ABC):
    @abstractmethod
    def get_info(self):
        self.name = input("enter your name :- ")
        self.age = int(input("enter your age :- "))
        self.mobile = int(input("enter your mobile number:- "))

        
    
    @abstractmethod
    def show_info(self):
        return f"name is {self.name} and age i s{self.age} and mobile number is {self.mobile} "
    

class Student(Person):
    def get_roll(self):
        self.roll = int(input("enter your roll number:- "))
    def get_info(self):
        self.name = input("enter your name :- ")
        self.age = int(input("enter your age :- "))
        self.mobile = int(input("enter your mobile number:- "))
    def show_info(self):
        return f"name is {self.name} and age i s{self.age} and mobile number is {self.mobile} "
    
