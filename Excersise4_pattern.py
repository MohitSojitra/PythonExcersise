

row = int(input(" enter the number of rows :- "))
is_true = int(input(" enter 1 for direct or 0 for the reverse :- "))

i = 0;
j = 0
if is_true == 1:
    while(i<row):
        while(j<row):
            if j<=i:
                print("*",end = " ")
            j += 1
        print("\n")
        j = 0
        i += 1
else:
    while(i<row):
        while(j<row):
            if j>=i:
                print("*",end = " ")
            j += 1
        print("\n")
        j = 0
        i += 1