from datetime import datetime as dt
from time import time
import os

path = "notes.csv"


def add_note(path_to_file):
    try:
        with open(path_to_file, encoding='utf-8', mode='r+') as pb:
            pb.seek(0, os.SEEK_END)
            isempty = pb.tell()
            if (isempty == 0):
                note_id = 1
                note = note_architecture()
                note.insert(0, note_id)
            else:
                with open(path_to_file, encoding='utf-8', mode='r+') as pb:
                    for line in pb:
                        pass
                    note_id = int(line[1]) + 1
                    note = note_architecture()
                    note.insert(0, note_id)
        return note
    except FileNotFoundError:
        print('Укажите верный файл или путь к нему')


def note_architecture():
    time = dt.now().strftime('%H:%M:%S')
    header = input('Введите заголовок заметки: ')
    note_body = input('Введите тело заметки: ')
    note = [time, header, note_body]
    return note


def save(data):
    try:
        with open("notes.csv", 'a', encoding="utf-8") as file:
            file.write(f'{data}\n')
    except FileNotFoundError:
        with open("notes.csv", 'w', encoding="utf-8") as file:
            file.write('{}\n'.format(data))


def print_to_console(path_to_file):
    try:
        with open(path_to_file, encoding='utf-8') as file:
            print(' ID   Time create  Header     Note body')
            row = file.readlines()
            print(''.join(row))
    except FileNotFoundError:
        print('Укажите верный файл или путь к нему')


def search_note(word):
    ab = []
    flag = True
    with open("notes.csv", encoding='utf-8', mode='r') as pb:
        for line_no, line in enumerate(pb):
            if word in line[1]:
                flag = False
                ab.append(line)
                print(line)
        if flag:
            ab.append(f'Записка с ID {word} не найден!')
        return (ab)


# res = add_note(path)
# note = note_architecture()
# print(note[0])
# save(res)
# print_to_console(path)
search_note("5")
