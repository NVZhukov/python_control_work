from datetime import datetime as dt
from time import time
import csv

note_id = 1


def add_note():
    global note_id
    time = dt.now().strftime('%H:%M:%S')
    header = input('Введите заголовок заметки: ')
    note_body = input('Введите тело заметки: ')
    note = [time, note_id, header, note_body]
    note_id += 1
    return note


def save(data):
    try:
        with open('notes.csv', 'a', encoding="utf-8") as file:
            file_writer = csv.writer(
                file, delimiter=";", lineterminator="\r")
            file_writer.writerow(data)
    except FileNotFoundError:
        with open('notes.csv', 'w', encoding="utf-8") as file:
            file_writer = csv.writer(
                file, delimiter=";", lineterminator="\r")
            file_writer.writerow(data)


res = add_note()
save(res)
