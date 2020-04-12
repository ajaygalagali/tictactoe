onerow = ["1", "2", "3"]
tworow = ["4", "5", "6"]
threerow = ["7", "8", "9"]


def changetozero(number, changeone):
    global count
    if number == 1 or number == 2 or number == 3:
        if onerow[number - 1] != "O" and onerow[number - 1] != "X":
            onerow[number - 1] = "O"
            changeone = False
            count += 1
        else:
            print("Invalid Entry, Enter again.")

    elif number == 4 or number == 5 or number == 6:
        if tworow[number - 4] != "O" and tworow[number - 4] != "X":
            tworow[number - 4] = "O"
            changeone = False
            count += 1
        else:
            print("Invalid Entry, Enter again.")

    elif number == 7 or number == 8 or number == 9:
        if threerow[number - 7] != "O" and threerow[number - 7] != "X":
            threerow[number - 7] = "O"
            changeone = False
            count += 1
        else:
            print("Invalid Entry, Enter again.")
    # else:
    # print("Invalid Entry")
    # changeone = True

    return changeone


def changetocross(number, changetwo):
    global count
    if number == 1 or number == 2 or number == 3:
        if onerow[number - 1] != "O" and onerow[number - 1] != "X":
            onerow[number - 1] = "X"
            changetwo = False
            count += 1
        else:
            print("Invalid Entry, Enter again.")

    elif number == 4 or number == 5 or number == 6:
        if tworow[number - 4] != "O" and tworow[number - 4] != "X":
            tworow[number - 4] = "X"
            changetwo = False
            count += 1
        else:
            print("Invalid Entry, Enter again.")

    elif number == 7 or number == 8 or number == 9:
        if threerow[number - 7] != "O" and threerow[number - 7] != "X":
            threerow[number - 7] = "X"
            changetwo = False
            count += 1
        else:
            print("Invalid Entry, Enter again.")
    # else:
    # print("Invalid Entry")
    # changetwo = True

    return changetwo


def check_win_one():
    global win
    if onerow[0] == "O" and onerow[1] == "O" and onerow[2] == "O":
        win=1

    if tworow[0] == "O" and tworow[1] == "O" and tworow[2] == "O":
        win=1

    if threerow[0] == "O" and threerow[1] == "O" and threerow[2] == "O":
        win=1

    if onerow[0] == "O" and tworow[1] == "O" and threerow[2] == "O":
        win=1

    if onerow[2] == "O" and tworow[1] == "O" and threerow[0] == "O":
        win=1

    if onerow[0] == "O" and tworow[0] == "O" and threerow[0] == "O":
        win=1

    if onerow[1] == "O" and tworow[1] == "O" and threerow[1] == "O":
        win=1

    if onerow[2] == "O" and tworow[2] == "O" and threerow[2] == "O":
        win=1

    # return 0


def check_win_two():
    global win
    if onerow[0] == "X" and onerow[1] == "X" and onerow[2] == "X":
        win=1

    if tworow[0] == "X" and tworow[1] == "X" and tworow[2] == "X":
        win=1

    if threerow[0] == "X" and threerow[1] == "X" and threerow[2] == "X":
        win=1

    if onerow[0] == "X" and tworow[1] == "X" and threerow[2] == "X":
        win=1

    if onerow[2] == "X" and tworow[1] == "X" and threerow[0] == "X":
        win=1

    if onerow[0] == "X" and tworow[0] == "X" and threerow[0] == "X":
        win=1

    if onerow[1] == "X" and tworow[1] == "X" and threerow[1] == "X":
        win=1

    if onerow[2] == "X" and tworow[2] == "X" and threerow[2] == "X":
        win=1

    # return 0


# Main

print("-----------------------------------------------------------------------------------------------")
print("                                       Welcome to TicTacToe                                    ")
print("                                                                       Coded by : Ajay Galagali")
print("-----------------------------------------------------------------------------------------------")

print("\n", onerow, "\n", tworow, "\n", threerow)
count = 0
win=0

# Logic
while 1:
    # Player 1
    changedone = True
    while changedone == True:
        playerone = int(input("Player 1 :"))
        changedone = changetozero(playerone, changedone)
        print("\n", onerow, "\n", tworow, "\n", threerow)
        check_win_one()
        if win ==1:
            print("===========================>    Player 1 Won    <===========================")
            print("===========================> Thanks For Playing <===========================")
            exit()
        if count == 9:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Its a TIE, Game Over~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("===========================> Thanks For Playing <===========================")
            exit()
    # Player 2
    changedtwo = True
    while changedtwo == True:
        playertwo = int(input("Player 2 :"))
        changedtwo = changetocross(playertwo, changedtwo)
        print("\n", onerow, "\n", tworow, "\n", threerow)
        check_win_two()
        if win ==1:
            print("===========================>    Player 2 Won    <===========================")
            print("===========================> Thanks For Playing <===========================")
            exit()
