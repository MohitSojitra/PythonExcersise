# here i will show ypu a how we use a for loop


list1 = ["mohit" , "parth" ,"manoj " , "mamu" , "kinjal" , 34, 54, 456]
dictionary1 = {"mohit" : "moylo" , "parth" : "vando" , "manoj" : "bahubally"}
for i, j in dictionary1.items():
    print(i,j)


list2 = ["mohit" , "mamu" , 45 ,54 , 23, 234, 2, 1, 3, 4, 5,6]

for item in list2:
    if str(item).isnumeric() and item > 6:
        print(item + " ")

