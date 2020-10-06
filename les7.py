# Выполните практическое задание для отработки пройденного материала. Проверьте себя, посмотрев разбор задания в следующем уроке.
#
# Проверка преподавателем в данном курсе не предусмотрена.
#
# Практическое задание
# Решить с помощью генераторов списка.
#
# 1: Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
#     Примечание: Списки фруктов создайте вручную в начале файла.
# 2: Дан список, заполненный произвольными числами. Получить список из элементов исходного, удовлетворяющих следующим условиям:
# Элемент кратен 3,
# Элемент положительный,
# Элемент не кратен 4.
#
# Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.
# 3. Напишите функцию которая принимает на вход список. Функция создает из этого списка новый список из квадратных корней чисел (если число положительное) и
# самих чисел (если число отрицательное) и возвращает результат (желательно применить генератор и тернарный оператор при необходимости). В результате работы
# функции исходный список не должен измениться.
# Например:
# old_list = [1, -3, 4]
# result = [1, -3, 2]
#
#     Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.
# 4. Написать функцию которая принимает на вход число от 1 до 100. Если число равно 13, функция поднимает исключительную ситуации ValueError иначе возвращает
# введенное число, возведенное в квадрат.
# Далее написать основной код программы. Пользователь вводит число. Введенное число передаем параметром в написанную функцию и печатаем результат,
# который вернула функция. Обработать возможность возникновения исключительной ситуации, которая поднимается внутри функции.

# 1: Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
#     Примечание: Списки фруктов создайте вручную в начале файла.

fruits_1 = ['apple', 'pineapple', 'orange']
fruits_2 = ['lemon', 'orange', 'banana', 'apple']

same_fruits = list(set([fruit for fruit in fruits_1 if fruit in fruits_2]))
# print(same_fruits)

# 2: Дан список, заполненный произвольными числами. Получить список из элементов исходного, удовлетворяющих следующим условиям:
# Элемент кратен 3,
# Элемент положительный,
# Элемент не кратен 4.

numbers = [1, 6, 2, -1, 7, 6, 12]
new_numbers = [number for number in numbers if number % 3 == 0 and number >= 0 and number%4 != 0]
# print(new_numbers)

# 3. Напишите функцию которая принимает на вход список. Функция создает из этого списка новый список из квадратных корней чисел (если число положительное) и
# самих чисел (если число отрицательное) и возвращает результат (желательно применить генератор и тернарный оператор при необходимости). В результате работы
# функции исходный список не должен измениться.
# Например:
# old_list = [1, -3, 4]
# result = [1, -3, 2]
#
#     Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.
from math import sqrt

old_list = [1, -3, 4]


def unsquare_list(some_list=[]):
    return [sqrt(number) if number >= 0 else number for number in some_list]


print(unsquare_list(old_list))
print(old_list)
# 4. Написать функцию которая принимает на вход число от 1 до 100. Если число равно 13, функция поднимает исключительную ситуации ValueError иначе возвращает
# введенное число, возведенное в квадрат.
# Далее написать основной код программы. Пользователь вводит число. Введенное число передаем параметром в написанную функцию и печатаем результат,
# который вернула функция. Обработать возможность возникновения исключительной ситуации, которая поднимается внутри функции.


def square(number=0):
    try:
        number = int(number)
        if number == 13:
            raise ValueError("несчастливое число")
        elif number <1 or number > 100:
            raise ValueError("не тот диапазон")
        else:
            number = number ** 2
    except ValueError as e:
        print(e.args[0])
    except Exception as e:
        print(e)
    else:
        print("Ошибок не было")
    finally:
        return number


value = input("Введите число от 1 до 100\n")
print(square(value))
