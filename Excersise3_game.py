
# created by Mr.sojitra
guess = 0
winNo = 12


while (1):
    print("guess nomber :- ")
    choice = int(input())
    guess = guess + 1
    if (guess == 9):
        print("game over ")
        break;
    elif (choice == winNo and guess != 9):
        print(" hey you win iphone x in " ,guess,"try" )
        break
    elif (choice > winNo and choice != 9):
        print("you choose big number please choose small number ")
        print("total " , 9 - guess , "try left keep trying ")
        continue
    else:
        print("you choose small number please choose big number ")
        print("total " , 9 - guess , "try left keep trying ")
        continue
