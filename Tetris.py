import os
import random
import sys, subprocess
import time
from pytimedinput import timedInput

def next_figure_fun(next_figure):
    if next_figure == "Z-l":
        draw = "[]\n[] []\n   []"

    elif next_figure == "Z-r":
        draw = "   []\n[] []\n[] "
    elif next_figure == "C":
        draw = "[] []\n[] []"
    elif next_figure == "I":
        draw = "[] [] [] []"
    elif next_figure == "T":
        draw = "[] [] []\n   []"
    elif next_figure == "G-l":
        draw = "[] []\n[]\n[]"
    elif next_figure == "G-r":
        draw = "[] []\n   []\n   []"
    else:
        draw = ""
    return draw


def field_strike_checker(saver_field):
    global points, HEIGHT
    new_field = saver_field
    counter_id = 0
    position = []
    for i in saver_field:
        strike = True
        for i2 in i:
            if i2 == 0:
                strike = False
                break

        if strike:
            points += 1
            position.append(counter_id)

        counter_id += 1
    if len(position) > 0:
        new_field = []
        for i2 in position:
            new_field.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            counter = 0
            for kolumn in saver_field:

                if counter < i2:
                    new_field.append(kolumn)
                elif counter > i2:
                    new_field.append(kolumn)
                counter += 1

            saver_field = new_field
            new_field = []

        new_field = saver_field

        return new_field
    else:
        return new_field


def action_checker(button, cords, type_figure, field, position_type):
    global cord_1, cord_1_1, cord_2, cord_2_1, cord_3, cord_3_1, cord_4, cord_4_1
    if button == 'a':
        available = True
        for cord in cords:
            for x in cord:
                if not cord[x] >= 1 or field[x][cord[x] - 1]:
                    return False, 0, position_type

        if available:
            return True, -1, position_type

        time.sleep(3)
    elif button == 'd':
        available = True
        for cord in cords:
            for x in cord:
                if not cord[x] < 9 or field[x][cord[x] + 1]:
                    return False, 0, position_type

        if available:
            return True, 1, position_type

        # right()
    elif button == ' ':
        if type_figure == "I":
            for cord in cords:
                for x in cord:
                    if position_type == "I-0":  # Checker
                        if cord_1 >= HEIGHT - 1 or field[cord_1 + 1][cord_1_1 + 1] == 1 or field[cord_3 - 1][
                            cord_3_1 - 1] == 1 or field[cord_4 - 2][cord_4_1 - 2] == 1:

                            return False, 0, "I-0"
                        else:
                            cord_1, cord_1_1 = cord_1 + 1, cord_1_1 + 1
                            cord_2, cord_2_1 = cord_2, cord_2_1
                            cord_3, cord_3_1 = cord_3 - 1, cord_3_1 - 1
                            cord_4, cord_4_1 = cord_4 - 2, cord_4_1 - 2
                            return True, 0, "I-1"
                    elif position_type == "I-1":
                        if cord_4 >= HEIGHT - 1 or field[cord_1 - 2][cord_1_1 - 1] == 1 or field[cord_2 - 1][
                            cord_2_1] == 1 or field[cord_3][cord_3_1 + 1] == 1 or field[cord_4 + 1][cord_4_1 + 2] == 1:
                            return False, 0, "I-1"
                        else:
                            cord_1, cord_1_1 = cord_1 - 2, cord_1_1 - 1
                            cord_2, cord_2_1 = cord_2 - 1, cord_2_1
                            cord_3, cord_3_1 = cord_3, cord_3_1 + 1
                            cord_4, cord_4_1 = cord_4 + 1, cord_4_1 + 2
                            return True, 0, "I-2"
                    elif position_type == "I-2":  # Checker
                        if field[cord_1 - 2][cord_1_1 + 2] == 1 or field[cord_2 - 1][cord_2_1 + 1] == 1 or \
                                field[cord_4 + 1][cord_4_1 - 1] == 1:
                            return False, 0, "I-2"
                        else:
                            cord_1, cord_1_1 = cord_1 - 2, cord_1_1 + 2
                            cord_2, cord_2_1 = cord_2 - 1, cord_2_1 + 1
                            cord_3, cord_3_1 = cord_3, cord_3_1
                            cord_4, cord_4_1 = cord_4 + 1, cord_4_1 - 1
                            return True, 0, "I-3"
                    elif position_type == "I-3":  # Checker
                        if field[cord_1 + 1][cord_1_1 - 2] == 1 or field[cord_2][cord_2_1 - 1] == 1 or \
                                field[cord_4 - 2][cord_4_1 + 1] == 1:
                            return False, 0, "I-3"
                        else:
                            cord_1, cord_1_1 = cord_1 + 3, cord_1_1 - 2
                            cord_2, cord_2_1 = cord_2 + 2, cord_2_1 - 1
                            cord_3, cord_3_1 = cord_3 + 1, cord_3_1
                            cord_4, cord_4_1 = cord_4, cord_4_1 + 1
                            return True, 0, "I-0"

        if type_figure == "Z-r":
            for cord in cords:
                for x in cord:
                    if position_type == "Z-r-0":  # Checker
                        if field[cord_1][cord_1_1 + 2] == 1:
                            return False, 0, "Z-r-0"
                        else:
                            cord_1, cord_1_1 = cord_1, cord_1_1 + 2
                            cord_2, cord_2_1 = cord_2, cord_2_1
                            cord_3, cord_3_1 = cord_3, cord_3_1
                            cord_4, cord_4_1 = cord_4 - 2, cord_4_1
                            return True, 0, "Z-r-1"
                    else:
                        if cord_4 >= HEIGHT - 2 or field[cord_1][cord_1_1 - 2] == 1:
                            return False, 0, "Z-r-1"
                        else:
                            cord_1, cord_1_1 = cord_1, cord_1_1 - 2
                            cord_2, cord_2_1 = cord_2, cord_2_1
                            cord_3, cord_3_1 = cord_3, cord_3_1
                            cord_4, cord_4_1 = cord_4 + 2, cord_4_1
                            return True, 0, "Z-r-0"
        if type_figure == "Z-l":
            for cord in cords:
                for x in cord:
                    if position_type == "Z-l-0":  # Checker
                        if cord_4 >= HEIGHT - 2 or field[cord_3][cord_3_1 + 2] == 1:
                            return False, 0, "Z-l-0"
                        else:
                            cord_1, cord_1_1 = cord_1, cord_1_1
                            cord_2, cord_2_1 = cord_2, cord_2_1
                            cord_3, cord_3_1 = cord_3, cord_3_1 + 2
                            cord_4, cord_4_1 = cord_4 - 2, cord_4_1
                            return True, 0, "Z-l-1"
                    else:
                        if cord_4 >= HEIGHT - 1 or field[cord_3 - 1][cord_3_1 - 2] == 1:
                            return False, 0, "Z-l-1"
                        else:
                            cord_1, cord_1_1 = cord_1 - 1, cord_1_1
                            cord_2, cord_2_1 = cord_2 - 1, cord_2_1
                            cord_3, cord_3_1 = cord_3 - 1, cord_3_1 - 2
                            cord_4, cord_4_1 = cord_4 + 1, cord_4_1
                            return True, 0, "Z-l-0"
        if type_figure == "G-l":
            for cord in cords:
                for x in cord:
                    if position_type == "G-l-0":  # Checker 0, 0+2, 0+1, 1+1, 1-1, 0+1, 2-2, 0
                        if cord_2 >= HEIGHT - 1 or field[cord_1][cord_1_1 + 2] == 1 or field[cord_2 + 1][
                            cord_2_1 + 1] == 1 or field[cord_3 - 1][cord_3_1 + 1] == 1:
                            return False, 0, "G-l-0"
                        else:
                            cord_1, cord_1_1 = cord_1, cord_1_1 + 2
                            cord_2, cord_2_1 = cord_2 + 1, cord_2_1 + 1
                            cord_3, cord_3_1 = cord_3 - 1, cord_3_1 + 1
                            cord_4, cord_4_1 = cord_4 - 2, cord_4_1
                            return True, 0, "G-l-1"

                    elif position_type == "G-l-1":  # Checker
                        if cord_4 >= HEIGHT - 1 or field[cord_2][cord_2_1 - 2] == 1 or field[cord_4 + 1][
                            cord_4_1 + 1] == 1:
                            return False, 0, "G-l-1"
                        else:
                            cord_1, cord_1_1 = cord_1, cord_1_1 - 1
                            cord_2, cord_2_1 = cord_2, cord_2_1 - 2
                            cord_3, cord_3_1 = cord_3 - 1, cord_3_1
                            cord_4, cord_4_1 = cord_4 + 1, cord_4_1 + 1
                            return True, 0, "G-l-2"
                    elif position_type == "G-l-2":  # Checker
                        if cord_3 >= HEIGHT - 2 or field[cord_1][cord_1_1 - 1] == 1 or field[cord_4][cord_4_1 + 1] == 1:
                            return False, 0, "G-l-2"
                        else:
                            cord_1, cord_1_1 = cord_1, cord_1_1 - 1
                            cord_2, cord_2_1 = cord_2, cord_2_1
                            cord_3, cord_3_1 = cord_3 + 2, cord_3_1
                            cord_4, cord_4_1 = cord_4, cord_4_1 + 1
                            return True, 0, "G-l-3"
                    elif position_type == "G-l-3":  # Checker 0, 0+2, 0+1, 1+1, 1-1, 0+1, 2-2, 0
                        if field[cord_3 - 1][cord_3_1 - 1] == 1 or field[cord_2 - 2][cord_2_1 + 1] == 1 or \
                                field[cord_4][cord_4_1 - 2] == 1:
                            return False, 0, "G-l-3"
                        else:
                            cord_1, cord_1_1 = cord_1 - 1, cord_1_1
                            cord_2, cord_2_1 = cord_2 - 2, cord_2_1 + 1
                            cord_3, cord_3_1 = cord_3 - 1, cord_3_1 - 1
                            cord_4, cord_4_1 = cord_4, cord_4_1 - 2
                            return True, 0, "G-l-0"
        if type_figure == "G-r":
            for cord in cords:
                for x in cord:
                    if position_type == "G-r-0":  # Checker 0, 0+2, 0+1, 1+1, 1-1, 0+1, 2-2, 0
                        try:
                            if cord_1 >= HEIGHT - 1 or field[cord_1 + 1][cord_1_1 - 1] == 1 or field[cord_2][
                                cord_2_1 - 2] == 1 or field[cord_3 - 1][cord_3_1 - 1] == 1:
                                return False, 0, "G-r-0"
                            else:
                                cord_1, cord_1_1 = cord_1 + 1, cord_1_1 - 1
                                cord_2, cord_2_1 = cord_2, cord_2_1 - 2
                                cord_3, cord_3_1 = cord_3 - 1, cord_3_1 - 1
                                cord_4, cord_4_1 = cord_4 - 2, cord_4_1
                                return True, 0, "G-r-1"
                        except:
                            print("Error")
                    elif position_type == "G-r-1":  # Checker
                        try:
                            if cord_2 >= HEIGHT - 1 or field[cord_1][cord_1_1 + 2] == 1 or field[cord_2 + 1][
                                cord_2_1 + 1] == 1 or field[cord_4 - 1][cord_4_1 - 1] == 1:
                                return False, 0, "G-r-1"
                            else:
                                cord_1, cord_1_1 = cord_1, cord_1_1 + 2
                                cord_2, cord_2_1 = cord_2 + 1, cord_2_1 + 1
                                cord_3, cord_3_1 = cord_3, cord_3_1
                                cord_4, cord_4_1 = cord_4 - 1, cord_4_1 - 1
                                return True, 0, "G-r-2"
                        except:
                            print("Error")
                    elif position_type == "G-r-2":  # Checker
                        try:
                            if cord_4 >= HEIGHT - 2 or field[cord_1 - 1][cord_1_1 + 1] == 1 or field[cord_2][
                                cord_2_1 + 2] == 1 or field[cord_3 + 1][cord_3_1 + 1] == 1:
                                return False, 0, "G-r-2"
                            else:
                                cord_1, cord_1_1 = cord_1 - 1, cord_1_1 + 1
                                cord_2, cord_2_1 = cord_2, cord_2_1 + 2
                                cord_3, cord_3_1 = cord_3 + 1, cord_3_1 + 1
                                cord_4, cord_4_1 = cord_4 + 2, cord_4_1
                                return True, 0, "G-r-3"
                        except:
                            print("Error")
                    elif position_type == "G-r-3":  # Checker 0, 0+2, 0+1, 1+1, 1-1, 0+1, 2-2, 0
                        try:
                            if field[cord_1 - 1][cord_1_1 - 1] == 1 or field[cord_3 - 1][cord_3_1 + 1] == 1 or \
                                    field[cord_4][cord_4_1 + 2] == 1:
                                return False, 0, "G-r-3"
                            else:
                                cord_1, cord_1_1 = cord_1 - 1, cord_1_1 - 1
                                cord_2, cord_2_1 = cord_2 - 2, cord_2_1
                                cord_3, cord_3_1 = cord_3 - 1, cord_3_1 + 1
                                cord_4, cord_4_1 = cord_4, cord_4_1 + 2
                                return True, 0, "G-r-0"
                        except:
                            print("Error")

        if type_figure == "T":
            for cord in cords:
                for x in cord:

                    if position_type == "T-0":
                        if cord_1 >= HEIGHT - 1:
                            return False, 0, "T-0"
                        else:
                            cord_1, cord_1_1 = cord_1 + 1, cord_1_1 + 1
                            cord_2, cord_2_1 = cord_2, cord_2_1
                            cord_3, cord_3_1 = cord_3, cord_3_1
                            cord_4, cord_4_1 = cord_4 - 2, cord_4_1
                            return True, 0, "T-1"

                    elif position_type == "T-1":  # Checker
                        if cord_4 >= HEIGHT - 2 or field[cord_3 + 1][cord_3_1 - 2] == 1 or field[cord_4 + 2][
                            cord_4_1] == 1 or field[cord_1][cord_1_1 + 1] == 1:
                            return False, 0, "T-1"
                        else:
                            cord_1, cord_1_1 = cord_1, cord_1_1 + 1
                            cord_2, cord_2_1 = cord_2, cord_2_1
                            cord_3, cord_3_1 = cord_3 + 1, cord_3_1 - 2
                            cord_4, cord_4_1 = cord_4 + 2, cord_4_1
                            return True, 0, "T-2"
                    elif position_type == "T-2":  # Checker
                        if cord_3 >= HEIGHT - 1 or field[cord_1][cord_1_1 - 2] == 1 or field[cord_3 + 1][
                            cord_3_1 + 1] == 1:
                            return False, 0, "T-2"
                        else:
                            cord_1, cord_1_1 = cord_1, cord_1_1 - 2
                            cord_2, cord_2_1 = cord_2, cord_2_1
                            cord_3, cord_3_1 = cord_3 + 1, cord_3_1 + 1
                            cord_4, cord_4_1 = cord_4, cord_4_1
                            return True, 0, "T-3"
                    elif position_type == "T-3":  # Checker 0, 1,0,2,0,3,1,2
                        if field[cord_3 - 2][cord_3_1 + 1] == 1:
                            return False, 0, "T-3"
                        else:
                            cord_1, cord_1_1 = cord_1 - 1, cord_1_1
                            cord_2, cord_2_1 = cord_2, cord_2_1
                            cord_3, cord_3_1 = cord_3 - 2, cord_3_1 + 1
                            cord_4, cord_4_1 = cord_4, cord_4_1
                            return True, 0, "T-0"
        if type_figure == "C":
            return False, 0, "C"

        time.sleep(3)

        # change()
    elif button == 's':
        return True, -10, position_type
        # down()


def main():
    global HEIGHT, points
    field = [[0 for _ in range(10)] for _ in range(15)]
    HEIGHT = 15
    points = 0
    list_of_figures = ["G-l", "G-r", "Z-l", "Z-r", "C", "T", "I"]  # "I",
    random_figure = random.choice(list_of_figures)
    random_figure_2 = random.choice(list_of_figures)
    random_figure_3 = random.choice(list_of_figures)
    while True:
        next_figure = [random_figure, random_figure_2, random_figure_3]
        field_1 = run_game(HEIGHT, field, random_figure, next_figure)
        if not field_1:
            print(f"The end. Your score:{points}")
            break
        random_figure = random.choice(list_of_figures)
        next_figure = [random_figure_2, random_figure_3, random_figure]

        field_2 = run_game(HEIGHT, field_1, random_figure_2, next_figure)
        if not field_2:
            print(f"The end. Your score:{points}")
            break
        random_figure_2 = random.choice(list_of_figures)
        next_figure = [random_figure_3, random_figure, random_figure_2]
        field = run_game(HEIGHT, field_2, random_figure_3, next_figure)
        if not field:
            print(f"The end. Your score:{points}")
            break

        # new_field = run_game(HEIGHT, field, random_figure)
        #
        #
        # if not new_field:
        #     print(f"The end. Your score:{points}")
        #     break
        #
        # field = run_game(HEIGHT, new_field, random_figure_2)
        # if not field:
        #     print(f"The end. Your score:{points}")
        #     break


def run_game(HEIGHT, field, type_figure, next_figure):
    global position_type, cord_1, cord_1_1, cord_2, cord_2_1, cord_3, cord_3_1, cord_4, cord_4_1, points
    next_is_break = False
    saver_field = []
    action_list = []
    move = False
    if type_figure == "Z-r":
        position_type = "Z-r-0"
        cord_1, cord_1_1, cord_2, cord_2_1, cord_3, cord_3_1, cord_4, cord_4_1 = 1, 4, 1, 5, 0, 5, 2, 4
    elif type_figure == "Z-l":
        position_type = "Z-l-0"
        cord_1, cord_1_1, cord_2, cord_2_1, cord_3, cord_3_1, cord_4, cord_4_1 = 1, 4, 1, 5, 0, 4, 2, 5
    elif type_figure == "G-l":
        position_type = "G-l-0"
        cord_1, cord_1_1, cord_2, cord_2_1, cord_3, cord_3_1, cord_4, cord_4_1 = 0, 4, 0, 5, 1, 4, 2, 4
    elif type_figure == "G-r":
        position_type = "G-r-0"
        cord_1, cord_1_1, cord_2, cord_2_1, cord_3, cord_3_1, cord_4, cord_4_1 = 0, 4, 0, 5, 1, 5, 2, 5
    elif type_figure == "T":
        position_type = "T-0"
        cord_1, cord_1_1, cord_2, cord_2_1, cord_3, cord_3_1, cord_4, cord_4_1 = 0, 3, 0, 4, 0, 5, 1, 4
    elif type_figure == "I":
        position_type = "I-0"
        cord_1, cord_1_1, cord_2, cord_2_1, cord_3, cord_3_1, cord_4, cord_4_1 = 0, 2, 0, 3, 0, 4, 0, 5
    else:
        position_type = "C"
        cord_1, cord_1_1, cord_2, cord_2_1, cord_3, cord_3_1, cord_4, cord_4_1 = 0, 4, 0, 5, 1, 4, 1, 5
    stop = False
    unlow_move = True
    for i in range(HEIGHT + 1):
        os.system('cls')
        counter = 0
        if not next_is_break:
            print(f"Your's points score:{points}")

            for i2 in field:
                if counter == 0:
                    if field[cord_1][cord_1_1] == 1 or field[cord_2][cord_2_1] == 1 or field[cord_3][cord_3_1] == 1 or field[cord_4][cord_4_1] == 1:
                        next_is_break = True
                        stop = True
                        break

                cords = [{cord_1: cord_1_1}, {cord_2: cord_2_1}, {cord_3: cord_3_1}, {cord_4: cord_4_1}]
                if move and unlow_move:
                    if len(action_list) == 0:
                        check, action, position_type = action_checker(button, cords, type_figure, field, position_type)
                    else:
                        for i in action_list:
                            check, action, position_type = action_checker(i, cords, type_figure, field, position_type)
                        action_list = []

                    if check:
                        if action == -10:
                            unlow_move = False
                            time.sleep(0.5)
                        else:
                            cord_1_1 = cord_1_1 + action
                            cord_2_1 = cord_2_1 + action
                            cord_3_1 = cord_3_1 + action
                            cord_4_1 = cord_4_1 + action

                    button = ""
                    move = False

                for cord in cords:
                    for x in cord:
                        if x == counter:

                            field[counter][cord[x]] = 1
                            if counter != HEIGHT - 1:
                                if field[counter + 1][cord[x]] != 1:
                                    pass
                                else:
                                    next_is_break = True

                            elif counter == HEIGHT - 1:
                                next_is_break = True
                                break

                # Printing file

                for i3 in i2:
                    if i3 == 0:
                        print("--", end=" ")
                    else:
                        print("[]", end=" ")
                print()

                # Create a scale of last dict
                for cord in cords:
                    for x in cord:
                        if x == counter:
                            if next_is_break:

                                break
                            else:
                                field[counter][cord[x]] = 0
                counter += 1
        else:
            # Save last snapshot of dict
            cord_1 -= 1
            cord_2 -= 1
            cord_3 -= 1
            cord_4 -= 1
            saver_field = []
            for i2 in field:
                cords = [{cord_1: cord_1_1}, {cord_2: cord_2_1}, {cord_3: cord_3_1}, {cord_4: cord_4_1}]

                for cord in cords:
                    for x in cord:
                        if x == counter:
                            field[counter][cord[x]] = 1

                copy_of_field = i2
                saver_field.append(copy_of_field)
                # Create a scale of last dict
                for cord in cords:
                    for x in cord:
                        if x == counter:
                            if next_is_break:
                                break
                            else:
                                field[counter][cord[x]] = 0
                counter += 1
            if next_is_break:  # Exit of loop
                os.system('cls')  # cls

                break
        if not stop:
            print("Next figure will be:\n")
            print("1.")
            print(next_figure_fun(next_figure[1]))
            print()
            print("2.")
            print(next_figure_fun(next_figure[2]))

        cord_1 += 1
        cord_2 += 1
        cord_3 += 1
        cord_4 += 1
        if unlow_move:
            if points <= 5:
                button, _ = timedInput("", timeout=0.55)
            elif points <= 15:
                button, _ = timedInput("", timeout=0.35)
            elif points <= 25:
                button, _ = timedInput("", timeout=0.2)
            else:
                button, _ = timedInput("", timeout=0.1)

            if button == "aaa" or button == "aa" or button == "aaaa":
                button = "a"
                move = True
            if button == "ddd" or button == "dd" or button == "dddd":
                button = "d"
                move = True

            if button == " a":
                move = True
                action_list.append(" ")
                action_list.append("a")
            elif button == " d":
                move = True
                action_list.append(" ")
                action_list.append("d")
            if button == "a" or button == " " or button == "s" or button == "d":
                move = True
    if stop:
        return []
    else:
        saver_field = field_strike_checker(saver_field)
        return saver_field


if __name__ == '__main__':
    main()

# python C:\Python\Projects\OwnProjects\GeniusGames\Tetris.py
