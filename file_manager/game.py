# 1. В этой игре человек загадывает число, а компьютер пытается его угадать.
# В начале игры человек загадывает число от 1 до 100 в уме или записывает его на листок бумаги. Компьютер начинает его отгадывать предлагая игроку варианты чисел. Если компьютер угадал число,
# игрок выбирает “победа”. Если компьютер назвал число меньше загаданного, игрок должен выбрать “загаданное число больше”. Если компьютер назвал число больше, игрок должен выбрать
# “загаданное число меньше”. Игра продолжается до тех пор пока компьютер не отгадает число.
# Пример игры:
# Допустим, пользователь загадал число 42

#     Примечание: Знаки “=”, “>” и “<” пользователь вводит с клавиатуры для общения с компьютером. Вы можете использовать этот способ или придумать свой.


def start_game():
    print("Загадайте число ")
    min_value = 1
    max_value = 100
    answer = 50
    count = 0
    while True:
        count += 1
        user_val = (input(
            f"Ответ {answer}? \nДля ответа введите >, если загаданное число больше, < - если меньши или =, если угадал."))
        if user_val == ">":
            min_value = answer
            answer = int((max_value + answer) / 2)
        elif user_val == "<":
            max_value = answer
            answer = int((answer + min_value) / 2)
        elif user_val == "=":
            print(f"Ура, я угадал! Число: {answer}")
            print(f"Ушло попыток: {count}")
            break
        else:
            print("Что-то тут не так")
