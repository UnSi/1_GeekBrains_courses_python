import os
import shutil
import datetime


def create_file(name, text=None):
    with open(name, "w", encoding="utf-8") as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError as e:
        print("Такая папка уже сущетсвует")


def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
        print("Список папок:")
    else:
        print("Список файлов и папок:")
    for path in result:
        print(path)


def delete_file(name):
    try:
        if os.path.isdir(name):
            os.rmdir(name)
        else:
            os.remove(name)
    except Exception as e:
        print(e)


def copy_file(name, new_name):
    if os.path.exists(name):
        if os.path.isdir(name):
            try:
                shutil.copytree(name, new_name)
            except FileExistsError:
                print("Такая папка уже есть")
        else:
            shutil.copy(name, new_name)
    else:
        print("Файла не существует")


def save_info(message):
    current_time = datetime.datetime.now()
    result = f"{current_time} - {message}"
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def change_path(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print("Путь не найден")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # create_folder('new_f')
    # get_list()
    # delete_file('1.dat')
    change_path('123')