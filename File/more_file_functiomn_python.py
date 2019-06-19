
with open("mohit.txt") as f1:
    print(f1.tell())
    print(f1.readline());
    print(f1.tell())
    f1.seek(24)
    print(f1.readline());
    print(f1.tell())
    print(f1.readline());

f1 = open("mohit.txt")
print(f1.tell())
print(f1.readline());
print(f1.tell())
f1.seek(20)
print(f1.readline());
print(f1.tell())
print(f1.readline());