


def exe1(fun):
    def exe2():
        print("now its executing")
        fun()
        print("hiii")
    return exe2

@exe1
def mohit():
    print("mohit is good boy")

mohit() 