
import os


def soldier(p,f1,f):
    os.chdir(p)
    l1 = os.listdir();
    i = 1
    file = open(f1);
    filer = file.read().split("\n")
    for name in l1:
        if f".{f}" in name and name not in filer:
            os.renames(name , f"{i}.{f}")
            i+=1
        else:
            if name in filer:
                pass
            else:
                os.renames(name, name.capitalize())

if __name__ == '__main__':
    p = input("enter the path:- ")
    f1 = input("enter file name:- ")
    f = input("enter the extension which you ordered:- ")

    soldier(p,f1,f)
