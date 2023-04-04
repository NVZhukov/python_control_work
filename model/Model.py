from datetime import datetime as dt
from time import time
import csv
import os

path = "notes.csv"


def add_note(path_to_file):
    try:
        with open(path_to_file, encoding='utf-8', mode='r+') as pb:
            pb.seek(0, os.SEEK_END)
            isempty = pb.tell()
            if (isempty == 0):
                note_id = 1
                time = dt.now().strftime('%H:%M:%S')
                header = input('Введите заголовок заметки: ')
                note_body = input('Введите тело заметки: ')
                note = [note_id, time, header, note_body]
                return note
            else:
                with open(path_to_file, encoding='utf-8', mode='r+') as pb:
                    for line in pb:
                        pass
                    note_id = int(line[1]) + 1
                    time = dt.now().strftime('%H:%M:%S')
                    header = input('Введите заголовок заметки: ')
                    note_body = input('Введите тело заметки: ')
                    note = [note_id, time, header, note_body]
                    return note
    except FileNotFoundError:
        print('Укажите верный файл или путь к нему')


def save(data):
    try:
        with open("notes.csv", 'a', encoding="utf-8") as file:
            file.write('{}\n'.format(data))
    except FileNotFoundError:
        with open("notes.csv", 'w', encoding="utf-8") as file:
            file.write('{}\n'.format(data))


def load(path_to_file):
    try:
        with open(path_to_file, encoding='utf-8', mode='r+') as pb:
            lines = pb.readlines()
            print(''.join(lines))
    except FileNotFoundError:
        print('Укажите верный файл или путь к нему')


res = add_note(path)
save(res)
# load(path)
