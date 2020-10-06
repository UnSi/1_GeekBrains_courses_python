# -------------------- Открытие, чтение, запись файлов -------------------------
'''
# open("filenamme", "param")
# params: r - чтение, w - запись (если нет - создаст) , x - запись (если нет - ошибка), a - (дозапись), b - двоичный,
# + - чтение и запись

# f = open("file_opening_test", "w")
# f.write("hello! \n")
# f.writelines(["1234\n","123\n"])

f = open("file_opening_test", "r")
print(f.read())
# for line in f:
#     print(line.replace("\n",""))
# print(f.readlines())
f.close()

with open("file_opening_test", "r") as f:
    print(f.readlines())
'''
# -------------------- Строки, байты -------------------------

# s = 'Hello world привет'
# sb = b'Hello bytes'
# print(type(sb))
# print(s[1])
# print(sb[1])
# print(s[1:3])
# print(sb[1:3])
# sb_2 = s.encode("utf-8")
# print(type(sb_2))
# print(sb_2)
# s_2 = sb_2.decode("utf-8")
# print(s_2)
# print(type(s_2))

# -------------------- Байты, работа с файлами -------------------------

# with open("file_bytes.txt", "wb") as f:
#     f.write(b"Something")
#
#
# with open("file_bytes.txt", "r", encoding="ascii") as f:
#     print(f.read())
#
# with open("file_bytes.txt", "wb") as f:
#     str = "Привет мир"
#     f.write(str.encode("utf-8"))
#
#
# with open("file_bytes.txt", "r", encoding="utf-8") as f:
#     print(f.read())

# -------------------- Байты, работа с файлами -------------------------
'''
person = {"name": "MAX",
          "phones":[123,324]}

with open("person.dat", "wb") as f:
        name = person["name"]
        f.write(f"{name}\n".encode("utf-8"))
        phones = person["phones"]
        for phone in phones:
            f.write(f"{phone}\n".encode("utf-8"))
        print("Объект записан")


with open("person.dat", "rb") as f:
        result = f.readlines()

new_person = {}

new_person["name"] = result[0].decode("utf-8").replace("\n","")
phones = []
for bphone in result[1:]:
        phones.append(bphone.decode("utf-8").replace("\n",""))
new_person["phones"] = phones

print(new_person)
'''
# -------------------- pickle -------------------------
# dump - сохраняет объект в файл
# dumps - преобразовывает объект в байты
# load - загрузка объекта из файла
# loads - загрузка из набора байт
'''
import pickle


person = {
        "name": "Max",
        "phones": [123,3241]
}

with open("person.dat", 'wb') as f:
        pickle.dump(person, f)
        print("Объект записан")


with open("person.dat", 'rb') as f:
        person = pickle.load(f)
        print(person)
'''
# -------------------- json -------------------------

import json


friends = [{
    "name":"Max",
    "age": 23,
    "phones": [123,321]
},{
    "name": "Leo",
    "age": 33
}]

#загнать в переменную
json_friends = json.dumps(friends)
print(type(friends))
print(type(json_friends))

#вытащить в переменную со строки джсон
new_friends = json.loads(json_friends)
print(new_friends)
print(type(new_friends))

#загнать в файл
with open("person.dat", "w") as f:
    json.dump(friends, f)

#вытащить с файла
with open("person.dat", "r") as f:
    json_friends = json.load(f)

