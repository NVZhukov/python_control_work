from model.View import *
from model.Model import *


def notes():
    path = get_path()
    while True:
        a = choose_action()
        if a == 1:
            find_note = message()
            res = search_note(path, find_note)
        elif a == 2:
            res = add_note(path)
            save(path, res)
        elif a == 3:
            data = message()
            res = delete_note(path, data)
        elif a == 4:
            data = message()
            param = change_note()
            res = change(path, data, param)
        elif a == 5:
            print_to_console(path)
        elif a == 6:
            break
