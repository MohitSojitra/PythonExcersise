
i = 1
computer_win = 0;
win = 0
tie1 = 0

def computer_win_match():
    global computer_win 
    computer_win += 1
    print(" you loss \n")
    print(f"computer win {computer_win} time")
    print(f"you win {win} time")
    print(f"total tie {tie1} match\n")
    print("choice again \n")

def tie():
    
    print("tie\n")
    
    global tie1
    tie1 += 1
    print(f"computer win {computer_win} time")
    print(f"you win {win} time")
    print(f"total tie {tie1} match\n")
    print("choice again \n")

def you_win():
    print(" you win \n")
    global win 
    win += 1
    print(f"computer win {computer_win} time")
    print(f"you win {win} time")
    print(f"total tie {tie1} match\n")
    print("choice again \n")

while i<=10:
    if i > 1:
        print("press 1: continue ")
        print("press 2: exit ")
        ch1 = input()

        if(ch1 == "2"):
            print(f" you win :- {win} times")

            print(f" you loss :- {computer_win} times") 
            break

    import random
    list = ["snake" , "water" , "gun"]
    choice = random.choice(list);
    print("press 1: snake ")
    print("press 2: water ")
    print("press 3: gun \n")
    print("enter your choice ")
    ch = input()
    print(f"computer choice is {choice}\n ")
    if choice == "snake" and ch == "1":
        i = i + 1
        tie()
        
    elif choice == "snake" and ch == "2":
        computer_win_match()
        i = i + 1
        
    elif choice == "snake" and ch == "3":
        you_win()
        i = i + 1
        
    elif choice == "water" and ch == "1":
        you_win()
        i = i + 1
        
    elif choice == "water" and ch == "2":
        tie()
        i = i + 1
        
    elif choice == "water" and ch == "3":
        computer_win_match()
        i = i + 1
      
    elif choice == "gun" and ch == "1":
        computer_win_match()
        i = i + 1
        
    elif choice == "gun" and ch == "2":
        you_win()
        i = i + 1
        
    elif choice == "gun" and ch == "3":
        tie()
        i = i + 1
        
    else:
        print("invalid choice ")
        print("please choice again ")
    if( i == 11):
        print("game over ")
        print(f"computer win {computer_win} time")
        print(f"you win {win} time")
        print(f"total tie {tie1} match")
        break;