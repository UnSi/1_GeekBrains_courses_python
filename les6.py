# is_has_name = False
# name = 'Max' if is_has_name else 'Empty'
# print(name)
#
# is_one = True
# number = 1 if is_one else 2
# print(number)
#
# is_russian = True
# print('Привет' if is_russian else 'Hello')
#
'''
word = "слово"

result = []
for i in range(len(word)):
    letter = word[i]
    letter = letter.lower() if i%2 != 0 else letter.upper()
    result.append(letter)

result = ''.join(result)
print(result)

numbers = [1, 2, 3, 4, 5, -1, -2, -3]

result = [number for number in numbers if number > 0]
print(result)

pairs = [(1, 'a'), (2, 'b'),(3, 'c')]

result = {pair[0]:pair[1] for pair in pairs}
print(result)

# для bool - False - пустые строки, списки, число 0. True - всё остальное
new_str = 'avax'
print('строка не пустая' if new_str else "строка пустая")

print([1] and 1 and 20 and 1.1 and None and 1) # вернет первый False, если нет - последний True
print([] or 0 or 0 or 0.0 or None or 1) # вернет первый True, если нет - последний False


# записать числа, кв. корень которых меньше 2х
import math

numbers = [1, 2, 3, 4, 5, -1, -2, -3]
numbers = [number for number in numbers if number > 0 and math.sqrt(number)<2]
print(numbers)
'''
# копирование списков
'''
a = [1, 2, [0, 7]]
b = a[:]  # создаёт не ссылку, а новый список, без учёта вложенных списков
b[1] = 5
print(a, "\n", b)

b = a
b = a.copy() # создаёт не ссылку, а новый список, без учёта вложенных списков
b[1] = 200
print(a, "\n", b)

b = list(a) # создаёт не ссылку, а новый список, без учёта вложенных списков
b[2][1] = 200
print(a)
b[2][1] = 7
import copy

b = copy.deepcopy(a) # создаёт полную копию списка  
b[2][1] = 200
print(a)
'''

number = int(input("Введите число: \n"))
try:
    result = 100 / number
except ZeroDivisionError as e:
    print('Деление на 0')
    print("Ошбика: ", e)
except Exception as e:
    print("Неизвестная ошибка")
    print("Информация:", e)
else:
    print("Ошибок не было")
finally:
    print("Полюбасу выполнится")

raise Exception("что-то пошло не так")
# специально вызвать исключение