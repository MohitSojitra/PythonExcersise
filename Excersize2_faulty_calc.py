# its a faulty calc if you want to try mul , division ypu get wrong answer

num1 = int(input("enter your first value :- "))
op = input("enter your operator : - ")
num2 = int(input("enter your second value :- "))

if op == "*":
    print("multiplicaton" , num1 * num2 + num2 )
elif op == "/":
    print("division " , num1 / num2 + num1)
elif op == "+":
    print("addition is " , num1 + num2)
elif op == "-":
    print("substraction is ", num1 - num2)
else:
    print("wrong operator you enterd ")
