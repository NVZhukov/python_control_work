from datetime import datetime as dt
import os
import glob


def add_note(path_to_file):
    try:
        with open(path_to_file, encoding='utf-8', mode='r+') as pb:
            pb.seek(0, os.SEEK_END)
            isempty = pb.tell()
            if (isempty == 0):
                note_id = 1
                note = f'{note_id}' + note_architecture()
            else:
                with open(path_to_file, encoding='utf-8', mode='r+') as pb:
                    for line in pb:
                        pass
                    note_id = int(line.split(';')[0]) + 1
                    note = f'{note_id}' + note_architecture()
        return note
    except FileNotFoundError:
        print('Укажите верный файл или путь к нему')


def note_architecture():
    time = dt.now().strftime("%d.%m.%Y %H:%M:%S")
    header = input('Введите заголовок заметки: ')
    note_body = input('Введите тело заметки: ')
    note = f';{time};{header};{note_body}'
    return note


def save(path_to_file, data):
    try:
        with open(path_to_file, 'a', encoding="utf-8") as file:
            file.write(f'{data}\n')
    except FileNotFoundError:
        with open(path_to_file, 'w', encoding="utf-8") as file:
            file.write('{}\n'.format(data))


def print_to_console(path_to_file):
    try:
        with open(path_to_file, encoding='utf-8') as file:
            for line in file:
                row = line.split(';')
                print(
                    f'ID: {row[0]} Time create: {row[1]} Header: {row[2]} Note body: {row[3]}')
    except FileNotFoundError:
        print('Укажите верный файл или путь к нему')


def search_note(path_to_file, word):
    ab = []
    flag = True
    with open(path_to_file, encoding='utf-8', mode='r') as pb:
        for line_no, line in enumerate(pb):
            if word in line.split(';')[0]:
                flag = False
                ab.append(line)
                row = line.split(';')
                print(
                    f'ID: {row[0]} Time create: {row[1]} Header: {row[2]} Note body: {row[3]}')
        if flag:
            print(f'Записка с ID {word} не найдена!\n')
        return (ab)


def delete_note(path_to_file, data):
    with open(path_to_file, encoding='utf-8', mode='r+') as pb:
        lines = pb.readlines()
        for line in lines:
            if data in line.split(';')[0]:
                file = open(path_to_file,
                            encoding='utf-8', mode='r')
                f = file.read().replace(line, '')
                f2 = open(path_to_file,
                          encoding='utf-8', mode='w')
                f2.write(f)
                f2.close()
                file.close()


def change(path_to_file, data, param):
    with open(path_to_file, encoding='utf-8', mode='r') as pb:
        lines = pb.readlines()
        for line in lines:
            if data in line.split(';')[0]:
                b = line.split(';')
                b[param + 1] = input('Введите новые данные:')
                file = open(path_to_file,
                            encoding='utf-8', mode='r')
                f = file.read().replace(line, ';'.join(b))
                f2 = open(path_to_file,
                          encoding='utf-8', mode='w')
                f2.write(f)
                f2.write('\n')
                f2.close


def get_path():
    path_dir = 'd:\\python\\control_work\\notes\\'
    if os.path.isdir(path_dir):
        if not os.listdir(path_dir):
            file_name = input('Укажите имя файла новой заметки: ')
            new_note = path_dir + file_name + '.csv'
            with open(new_note, 'wb') as myfile:
                return new_note
        else:
            print('Вот такие есть заметки:')
            extension = 'csv'
            os.chdir(path_dir)
            result = glob.glob('*.{}'.format(extension))
            for names in result:
                print(names)
            file_name = input('Укажите имя файла с которым хотите работать: ')
            path_dir = f'{file_name}.csv'
            if (path_dir != names):
                with open(path_dir, 'wb') as myfile:
                    return path_dir
    else:
        print("Given directory doesn't exist")

    return path_dir
