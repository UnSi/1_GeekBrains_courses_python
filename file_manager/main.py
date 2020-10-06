import sys
# не импортирует модули, надо перенести в корень проекта, чтоб работало
from core import get_list, delete_file, create_folder, create_file, copy_file, save_info, change_path
import game


def print_help():
    print('list - cписок файлов и папок')
    print('create_file - создание файла')
    print('create_folder - создание папки')
    print('delete - удаление файла или папки')
    print('copy - копирование файла или папки')
    print('cd - перейти в другую папку')
    print('play - играть')


save_info('старт')
try:
    command = sys.argv[1]
except IndexError:
    print_help()
    save_info('конец')
    sys.exit()

if command == 'list':
    get_list()
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print("Отсутствует название файла")
    else:
        create_file(name)
elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print("Отсутствует название папки")
    else:
        create_folder(name)
elif command == 'delete':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название файла/папки')
    else:
        delete_file(name)
elif command == 'copy':
    try:
        name = sys.argv[2]
    except IndexError as e:
        print("Отсутствует название копируемого файла")
    try:
        new_name = sys.argv[3]
    except IndexError:
        print("Отсутствует название нового файла")
    else:
        copy_file(name, new_name)
elif command == 'cd':
    try:
        folder = sys.argv[2]
    except IndexError:
        print('Отсутствует название файла/папки')
    else:
        change_path(folder)
elif command == 'play':
    game.start_game()
else:
    print_help()


save_info('конец')

# 1. В консольный файловый менеджер добавить проверку ввода пользователя для всех функции с параметрами (на уроке разбирали на примере одной функции).
# 2. Добавить возможность изменения текущей рабочей директории.
# 3. Добавить возможность развлечения в процессе работы с менеджером. Для этого добавить в менеджер запуск одной из игр: “угадай число” или “угадай число (наоборот)”.
