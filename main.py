# 3: Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций. Вызовите каждую функцию в main.py и проверьте что все работает как надо.
# Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1), так и отдельные функции из модуля.

import dir_creator.operation_center as oc
import les4

oc.new_dir()
oc.remove_dir()

print(les4.random_list_element([1,2,3,4]))

from dir_creator.operation_center import *
from les4 import random_list_element


new_dir(ERR_DIR)
remove_dir()
print(random_list_element([1,2]))
print(random_list_element([]))