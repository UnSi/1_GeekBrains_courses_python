# 2: Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент. Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
#     Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]
import random


def random_list_element (user_list=[]):
    if user_list:
        return random.choice(user_list)

# print(random_list_element([1,2,3,4]))
# print(random_list_element([]))

