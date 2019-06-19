a = 0;
b = 1
def fibonaki(l):
    if l == 0:
        return 0
    global a
    global b
    c = a + b
    a ,b = b , c
    print(c, end = " ")
    fibonaki( l - 1)





print("enter the limit : - ")
limit = int(input());
a = 0;
b = 1
print(a,b , end = " ")
fibonaki(limit - 2)