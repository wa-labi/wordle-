import random
from methods_for_wordle import *
import pickle

screen_clear()
open_file = open("new_allowed_five_words.pkl", "rb")
allowed_list = pickle.load(open_file)
open_file.close()

game_on = True
while game_on:
    key_dic = {'q': (0, 0), 'w': (0, 0), 'e': (0, 0), 'r': (0, 0), 't': (0, 0),
               'y': (0, 0), 'u': (0, 0), 'i': (0, 0), 'o': (0, 0), 'p': (0, 0),
               'a': (0, 0), 's': (0, 0), 'd': (0, 0), 'f': (0, 0), 'g': (0, 0),
               'h': (0, 0), 'j': (0, 0), 'k': (0, 0), 'l': (0, 0), 'z': (0, 0),
               'x': (0, 0), 'c': (0, 0), 'v': (0, 0), 'b': (0, 0), 'n': (0, 0), 'm': (0, 0)}

    a_file = open("data.pkl", "rb")
    five_wrd_dic = pickle.load(a_file)
    a_file.close()
    answer = ""
    while len(set(answer)) != 5:
        answer = random.choice(list(five_wrd_dic.keys()))

    word_meaning = five_wrd_dic[answer][0]
    word_example = five_wrd_dic[answer][1]

    shown_example = word_example.replace(answer or answer.capitalize(), "?????")
    hint_list = [word_meaning, shown_example]
    guess_time_on = True
    round_num = 0
    guess_count = 0
    hint_count = 0
    guess_lst = ""
    while guess_time_on:
        round_num += 1
        print("【ラウンド " + str(round_num) + "】")
        # selected_num = input("1:Hint or 2:Try: ")
        ply_inp = ""
        if hint_count != 2:
            while not (not any(ltr.isdigit() for ltr in ply_inp) and ((len(ply_inp) == 1 and ply_inp == "h") or (
                    len(ply_inp) == 5 and len(set(ply_inp)) == 5 and ply_inp in allowed_list))):
                try:
                    ply_inp = input("単語を答えてください (h:ヒント): ")
                except:
                    pass
        else:
            while not (not any(ltr.isdigit() for ltr in ply_inp) and len(ply_inp) == 5 and len(
                    set(ply_inp)) == 5 and ply_inp in allowed_list):
                ply_inp = input("単語を答えてください: ")

        if ply_inp == "h":
            print(hint_list[0])
            hint_count += 1
            del hint_list[0]
        else:
            guess_word = ply_inp.lower()
            guess_count += 1
            guess_lst += guess_word
            if guess_count == 1:
                new_board = check_rnd1(answer, guess_word, key_dic)
            else:
                new_board = check_rnd2_(answer, guess_word, key_dic, guess_count)
            show_board(new_board, guess_lst)
            show_keyboard(new_board)

            # screen_clear()

            if win_check(guess_count, new_board):
                print("所要回数: " + str(round_num) + "回")
                print("答え:", answer)
                guess_time_on = False
            else:
                pass
        print("")

    err_res = True
    while err_res:
        res = input("もう一度遊びますか? y/n: ").lower()
        if res in ("y", "n"):
            if res == "y":
                pass
            else:
                game_on = False
            err_res = False
        else:
            pass
        print("")

print("お疲れ様でした")
