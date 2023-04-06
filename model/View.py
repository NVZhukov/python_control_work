def choose_action():
    print(f"Выберите действие \nНайти определенную заметку - 1\nДобавить новую заметку - 2\n\
Удалить заметку - 3\nРедактировать заметку - 4\nВывести все заметки - 5\nВыход - 6")
    valid = False
    while not valid:
        player_answer = input()
        try:
            player_answer = int(player_answer)
            if player_answer >= 1 and player_answer <= 2:
                valid = True
            elif player_answer == 3:
                valid = True
            elif player_answer == 4:
                valid = True
            elif player_answer == 5:
                valid = True
            elif player_answer == 6:
                valid = True
            else:
                print("Такой команды нет.\nНекорректный ввод.")
        except:
            print("Некорректный ввод. Введите число")
            continue
    return player_answer


def change_note():
    print('Какое поле хотите изменить?')
    print(f"\nЗаголовок заметки - 1\nСодержание заметки - 2\n")
    valid = False
    while not valid:
        answer = input()
        try:
            answer = int(answer)
            if answer == 1:
                valid = True
            elif answer == 2:
                valid = True
            else:
                print("Такой команды нет.\nНекорректный ввод.")
        except:
            print("Некорректный ввод. Введите число")
            continue
    return answer


def message():
    return input("Укажите ID заметки: ")
