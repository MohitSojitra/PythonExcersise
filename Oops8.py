

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


class Player:
    def __init__(self , name, game):
        self.name = name
        self.game = game
    def print_details(self):
        print(f"the name is {self.name} amd play gamme is {self.game}")

class Cool_employee(Player , Employee):
    languages = ["pyhton ", "c#"]

    def print_info(self):
        print(f"he knows {self.languages} languages")



if __name__ == '__main__':

   mohit = Cool_employee("mohit" , ["cricket", "football"])
   mohit.print_info();
#    mohit.show_detail()
   mohit.print_details()