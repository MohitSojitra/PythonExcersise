


class Electronic_device:
    work_battery = 7
   
    def print_details(self):
        print(f"product name is  and working hour is {self.work_battery}")

    
class Gadget_device(Electronic_device):
    work_bettry = 5
    def __init__(self, name):
        self.name = name


class Phone(Gadget_device):
    pass



vivo = Phone("vivo")
vivo.print_details()
