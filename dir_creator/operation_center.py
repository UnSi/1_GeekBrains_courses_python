# Выполните практическое задание для отработки пройденного материала. Проверьте себя, посмотрев разбор задания в следующем уроке.
#
# Проверка преподавателем в данном курсе не предусмотрена.
#
# Практическое задание
# 1: Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py). В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код.
# Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.
# 2: Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент. Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
#     Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]
# 3: Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций. Вызовите каждую функцию в main.py и проверьте что все работает как надо.
# Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1), так и отдельные функции из модуля.
import os


CUR_DIR = os.getcwd()
ERR_DIR = "C:\\Program Files\\test\\"


def new_dir(folder=CUR_DIR):
    folder = str(folder)
    dirs = []
    for i in range(1,10):
        dirs.append(os.path.join(folder, "dir_" + str(i)))
        if not os.path.exists(dirs[i - 1]):
            try:
                os.mkdir(dirs[i-1])
                print("Создал", dirs[i-1])
            except Exception as exc:
                print(exc)
        else:
            print("Не создал, уже есть")


def remove_dir(folder=CUR_DIR):
    dirs = os.listdir(folder)
    for dir in dirs:
        for i in range (1,10):
            if str(dir) == "dir_" + str(i):
                os.rmdir(dir)
                print("Удалил", dir)


def input_dir_name():
    new_dir(input("Введите путь к дирректории, где создать папку "))


# remove_dir()
# new_dir(ERR_DIR)
# print("C:\\Program Files\\test\\")
# input_dir_name()
# print(CUR_DIR)
