import os
from os import system, name
import colorama
from colorama import Fore

colorama.init(autoreset=True)

key_dic = {'q': (0, 0), 'w': (0, 0), 'e': (0, 0), 'r': (0, 0), 't': (0, 0),
           'y': (0, 0), 'u': (0, 0), 'i': (0, 0), 'o': (0, 0), 'p': (0, 0),
           'a': (0, 0), 's': (0, 0), 'd': (0, 0), 'f': (0, 0), 'g': (0, 0),
           'h': (0, 0), 'j': (0, 0), 'k': (0, 0), 'l': (0, 0), 'z': (0, 0),
           'x': (0, 0), 'c': (0, 0), 'v': (0, 0), 'b': (0, 0), 'n': (0, 0), 'm': (0, 0)}


def show_board(keyboard_dic, inp_list):
    print(" _____ _____ _____ _____ _____")
    for row in range(1, int(len(inp_list) / 5) + 1):
        print("|     |     |     |     |     |")
        print("|", end="")
        for i in range(row * 5 - 5, row * 5):
            print("  ", end="")
            if keyboard_dic[inp_list[i]][row] == 3:  # ピッタリの場合みどり
                print(Fore.GREEN + inp_list[i], end="")
            elif keyboard_dic[inp_list[i]][row] == 2:  # ぴったりじゃないけど含まれて入るなら黄色
                print(Fore.YELLOW + inp_list[i], end="")
            else:  # 白
                print(Fore.WHITE + inp_list[i], end="")
            print("  |", end="")
        print("\n|_____|_____|_____|_____|_____|")


def prt_key(letters, keyboard_dic):
    for letter in letters:
        if 3 in keyboard_dic[letter]:  # ピッタリの場合みどり
            print(Fore.GREEN + letter, end="  ")
        elif 2 in keyboard_dic[letter]:  # ぴったりじゃないけど含まれて入るなら黄色
            print(Fore.YELLOW + letter, end="  ")
        elif 1 in keyboard_dic[letter]:  # black
            print(Fore.BLACK + letter, end="  ")
        else:  # white
            print(Fore.WHITE + letter, end="  ")


def show_keyboard(keyboard_dic):
    prt_key("qwertyuiop", keyboard_dic)
    print("\n", end="  ")
    prt_key("asdfghjkl", keyboard_dic)
    print("\n", end="    ")
    prt_key("zxcvbnm", keyboard_dic)
    print("")


def check_rnd1(answer_word, inp_word, keyboard_dic):
    for letter in range(5):
        if answer_word[letter] == inp_word[letter]:
            keyboard_dic[inp_word[letter]] = (0, 3)
        elif inp_word[letter] in answer_word:
            keyboard_dic[inp_word[letter]] = (0, 2)
        elif inp_word[letter] not in answer_word:
            keyboard_dic[inp_word[letter]] = (0, 1)
    return keyboard_dic


def check_rnd2_(answer_word, inp_word, keyboard_dic, num_of_guess):
    for letter_num in range(5):
        value_lst = list(keyboard_dic[inp_word[letter_num]])
        if answer_word[letter_num] == inp_word[letter_num]:
            value_lst.append(3)  # green
            keyboard_dic[inp_word[letter_num]] = tuple(value_lst)
        elif inp_word[letter_num] in answer_word:
            value_lst.append(2)  # yellow
            keyboard_dic[inp_word[letter_num]] = tuple(value_lst)
        else:
            value_lst.append(1)  # gone
            keyboard_dic[inp_word[letter_num]] = tuple(value_lst)
    for key in keyboard_dic:
        if len(keyboard_dic[key]) == num_of_guess:
            value_lst = list(keyboard_dic[key])
            value_lst.append(0)
            keyboard_dic[key] = tuple(value_lst)

    return keyboard_dic


def win_check(num_of_guess, keyboard_dic):
    green_count = 0
    for key in keyboard_dic:
        if keyboard_dic[key][num_of_guess] == 3:
            green_count += 1
        else:
            pass
    if green_count == 5 or num_of_guess == 6:
        return True
    else:
        return False


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')
