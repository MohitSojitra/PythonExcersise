

class Employee:
    banner = "pramod"
    _newBanner = "saran"
    __newNewBanner = "mama"
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





if __name__ == '__main__':
    
    mohit = Employee("mohit" , 89)
    print(mohit.banner)
    print(mohit._newBanner)
    print(mohit._Employee__newNewBanner)
    
