


class A:
    var1 = "this is a class A var1"

    def __init__(self):
        self.classvar = "inside a class A custroctor"
        self.var1 = "its changed in constructor A"
        self.special = "its compusory print A"

class B(A):
    def __init__(self):
        
        self.classvar = "inside a class B custroctor"
        self.var1 = "its changed in constructor B"
        super().__init__();


a = A()
b = B()

print(b.var1 , b.special)
