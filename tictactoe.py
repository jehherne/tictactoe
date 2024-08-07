import time
import random

def welcome(formation):
    original_formation = formation
    new_formation = [
    [" ", "|", " ", "|", " "],
    ["-", "|", "-", "|", "-"],
    [" ", "|", " ", "|", " "],
    ["-", "|", "-", "|", "-"],
    [" ", "|", " ", "|", " "]
]
    print("Welcome to the Tic-Tac-Toe Game")
    for row in range (len(new_formation)):
        for each_space in range (len(new_formation[row])):
            if each_space == 0:
                new_formation[row][each_space] = "           "+new_formation[row][each_space]                                                                               
    print_formation(new_formation)
    symbol = ["X","O"]
    random_symbol = symbol[random.randint(0,1)]
    if random_symbol == "X":
        com_symbol = "O"
    else:
        com_symbol = "X"
    print("Your Symbol is {}".format(random_symbol))
    print("\n")
    add_location(original_formation)
    add_symbol(random_symbol,com_symbol,original_formation)


def print_formation(formation):
    for row in formation:
        print(" ".join(row))

def add_location(formation):
    wait()
    number_assign = 1
    for row in range (len(formation)):
        for each_space in range (len(formation[row])):
            if formation[row][each_space] == " ":
                formation[row][each_space] = str(number_assign)
                number_assign +=1
    print_formation(formation)
    wait()
    rules()

def rules():
    print("To Locate Your Symbol on Any Space, Enter the Number Corresponding(1-9)")

def define_win(formation):
    every_space = []
    com = []
    required = [0,2,4]
    horizontal = [0,1,2]
    vertical = [0,3,6]
    for row in range (len(formation)):
        for each_space in range (len(formation[row])):
            if row in required and each_space in required:
                every_space.append(formation[row][each_space])
    for repeat_horizontal in range(3):
        if every_space[horizontal[0]] == every_space[horizontal[1]] == every_space[horizontal[2]]:
            return True,every_space[horizontal[0]],None,formation
        else:
            if every_space[horizontal[0]] == every_space[horizontal[1]] or every_space[horizontal[1]]==every_space[horizontal[2]] or every_space[horizontal[0]]==every_space[horizontal[2]]:
                for r in range(3):
                    if every_space[horizontal[r]]!="X" and every_space[horizontal[r]]!="O":
                        com.append(every_space[horizontal[r]])
                        continue
            for every in range (len(horizontal)):
                horizontal[every] = horizontal[every]+3
    for repeat_vertical in range(3):
        if every_space[vertical[0]] == every_space[vertical[1]] == every_space[vertical[2]]:
            return True,every_space[vertical[0]],None,formation
        else:
            if every_space[vertical[0]] == every_space[vertical[1]] or every_space[vertical[1]]==every_space[vertical[2]] or every_space[vertical[0]]==every_space[vertical[2]]:
                for r in range(3):
                    if every_space[vertical[r]]!="X" and every_space[vertical[r]]!="O":
                        com.append(every_space[vertical[r]])
                        continue
            for every in range (len(vertical)):
                vertical[every] = vertical[every]+1
    if every_space[0] == every_space[4] == every_space[8]:
        return True,every_space[0],None,formation
    if every_space[2] == every_space[4] == every_space[6]:
        return True,every_space[2],None,formation
    if every_space[0] == every_space[4] or  every_space[0] == every_space[8] or every_space[4] == every_space[8]:
            if every_space[0]!="X" and every_space[0]!="O":
                com.append("1")
            elif every_space[4]!="X" and every_space[4]!="O":
                com.append("5")
            else:
                com.append("9")

    if every_space[2] == every_space[4] or  every_space[4] == every_space[6] or every_space[2] == every_space[6]:
            if every_space[2]!="X" and every_space[2]!="O":
                com.append("3")
            elif every_space[4]!="X" and every_space[4]!="O":
                com.append("5")
            else:
                com.append("7")
    if every_space[2] == every_space[4] == every_space[6]:
        return True,every_space[2],None,formation
    return False,None,com,formation


def com_define_win(symbol,com_symbol,formation):
    every_space = []
    required = [0,2,4]
    horizontal = [0,1,2]
    vertical = [0,3,6]
    for row in range (len(formation)):
        for each_space in range (len(formation[row])):
            if row in required and each_space in required:
                every_space.append(formation[row][each_space])
    for repeat_horizontal in range(3):
        if every_space[horizontal[0]] == every_space[horizontal[1]] == every_space[horizontal[2]]:
            return True,formation
        else:
            for every in range (len(horizontal)):
                horizontal[every] = horizontal[every]+3
    for repeat_vertical in range(3):
        if every_space[vertical[0]] == every_space[vertical[1]] == every_space[vertical[2]]:
            return True,formation
        else:
            for every in range (len(vertical)):
                vertical[every] = vertical[every]+1
    if every_space[0] == every_space[4] == every_space[8]:
        return True,formation
    if every_space[2] == every_space[4] == every_space[6]:
        return True,formation
    return None,formation
    

def add_symbol(symbol,com_symbol,formation):
    every_placement = {"1":[0,0],"2":[2,0],"3":[4,0],"4":[0,2],"5":[2,2],"6":[4,2],"7":[0,4],"8":[2,4],"9":[4,4]}
    while True:
        placement = input("Enter a Number to Locate Your Symbol: ")
        if placement !="1" and placement !="2" and placement !="3" and placement !="4" and placement !="5" and placement !="6" and placement !="7" and placement !="8" and placement !="9":
            continue
        location = every_placement[placement]
        x = location[0]
        y = location[1]
        if formation[y][x] == "X" or formation[y][x] =="O":
            continue
        formation[y][x] = symbol
        check_end(formation,every_placement)
        condition,sym,com,formation = define_win(formation)
        if condition == True:
            print("You Win!")
            print_formation(formation)
            return
        situation,formation = com_play(formation,com,com_symbol,symbol,every_placement)
        if situation == True:
            print_formation(formation)
            print("You Lose!")
            return
        else:
            print_formation(formation)


def check_end(formation,every_placement):
    exit_count = 0
    numbers = ["1","2","3","4","5","6","7","8","9"]
    for every_position in every_placement.keys():
        location = every_placement[every_position]
        x = location[0]
        y = location[1]
        if formation[y][x]=="X" or formation[y][x]=="O":
            exit_count+=1
    if exit_count == 9:
        print_formation(formation)
        print("It's a Draw!")
        exit()


def com_play(formation,com,com_symbol,symbol,every_placement):
    while True:
        if com == []: 
            play = []
            every_space = []
            required = [0,2,4]
            horizontal = [0,1,2]
            vertical = [0,3,6]
            for row in range (len(formation)):
                for each_space in range (len(formation[row])):
                    if row in required and each_space in required:
                            every_space.append(formation[row][each_space])
            for repeat_horizontal in range(3):
                if every_space[horizontal[0]] == every_space[horizontal[1]] or every_space[horizontal[1]]==every_space[horizontal[2]] or every_space[horizontal[0]]==every_space[horizontal[2]]:
                    if every_space[horizontal[0]] != com_symbol and every_space[horizontal[1]]!=com_symbol:
                        break
                    for r in range(3):
                        if every_space[horizontal[r]]!="X" and every_space[horizontal[r]]!="O":
                            play.append(every_space[horizontal[r]])
                            continue
                for every in range (len(horizontal)):
                    horizontal[every] = horizontal[every]+3
            for repeat_vertical in range(3):
                if every_space[vertical[0]] == every_space[vertical[1]] or every_space[vertical[1]]==every_space[vertical[2]] or every_space[vertical[0]]==every_space[vertical[2]]:
                    if every_space[vertical[0]] != com_symbol and every_space[vertical[1]]!=com_symbol:
                        break
                    for r in range(3):
                        if every_space[vertical[r]]!="X" and every_space[vertical[r]]!="O":
                            play.append(every_space[vertical[r]])
                            continue
                for every in range (len(vertical)):
                    vertical[every] = vertical[every]+1
            if every_space[0] == every_space[4] or  every_space[0] == every_space[8] or every_space[4] == every_space[8]:
                if every_space[0] != com_symbol and every_space[4]!=com_symbol:
                        break
                if every_space[0]!="X" and every_space[0]!="O":
                    play.append("1")
                elif every_space[4]!="X" and every_space[4]!="O":
                    play.append("5")
                else:
                    play.append("9")

            if every_space[2] == every_space[4] or  every_space[4] == every_space[6] or every_space[2] == every_space[6]:
                    if every_space[horizontal[2]] != com_symbol and every_space[horizontal[4]]!=com_symbol:
                        break
                    if every_space[2]!="X" and every_space[2]!="O":
                        play.append("3")
                    elif every_space[4]!="X" and every_space[4]!="O":
                        play.append("5")
                    else:
                        play.append("7")
            if play == []:
                random_location = random.randint(1,9)
                location = every_placement[str(random_location)]
                x = location[0]
                y = location[1]
                if formation[y][x] == "X" or formation[y][x] =="O":
                    continue
                formation[y][x] = com_symbol
                return com_define_win(symbol,com_symbol,formation)
            else:
                    location = every_placement[str(play[0])]
                    x = location[0]
                    y = location[1]
                    if formation[y][x] == "X" or formation[y][x] =="O":
                        random_location = random.randint(1,9)
                        location = every_placement[str(random_location)]
                        x = location[0]
                        y = location[1]
                        if formation[y][x] == "X" or formation[y][x] =="O":
                            continue
                    formation[y][x] = com_symbol
                    return com_define_win(symbol,com_symbol,formation)
        location = every_placement[str(com[0])]
        x = location[0]
        y = location[1]
        if formation[y][x] == "X" or formation[y][x] =="O":
            random_location = random.randint(1,9)
            location = every_placement[str(random_location)]
            x = location[0]
            y = location[1]
            if formation[y][x] == "X" or formation[y][x] =="O":
                continue
        formation[y][x] = com_symbol
        return com_define_win(symbol,com_symbol,formation)


def wait():
    time.sleep(.5)

formation = [
    [" ", "|", " ", "|", " "],
    ["-", "|", "-", "|", "-"],
    [" ", "|", " ", "|", " "],
    ["-", "|", "-", "|", "-"],
    [" ", "|", " ", "|", " "]
]
welcome(formation)
