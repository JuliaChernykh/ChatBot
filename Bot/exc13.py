import random
import math

def text(concrete_str):
    if concrete_str[1] == 1:  # первый тип
        cur = concrete_str[3]
        length = random.randint(7, 12)  # генерируем длину пароля
        cur = cur.replace("#N1", str(length))  # меняем длину пароля
        amount_of_users = [20, 30, 40, 50, 60, 70, 80]
        users = random.choice(amount_of_users)  # генерируем количество пользователей
        cur = cur.replace("#N2", str(users))
        while True:  # генерируем память, которая потребовалась для хранения паролей
            memory = random.randint(300, 1000)
            if memory % users == 0 and memory / users > 12:
                break
        cur = cur.replace("#N3", str(memory))

        answer = exc13_1(length, users, memory)
        result = [cur, answer]
        return result
    if concrete_str[1] == 2:
        cur = concrete_str[3]
        length = random.randint(8, 15)  # генерируем длину пароля
        cur = cur.replace("#N1", str(length))  # меняем длину пароля
        numbers = [500, 600, 700, 800, 900, 1000]
        number = random.choice(numbers)  # генерируем номер подразделения
        cur = cur.replace("#N2", str(number))
        memory = random.randint(35, 60)
        cur = cur.replace("#N3", str(memory))
        answer = exc13_2(length, number, memory)
        result = [cur, answer]
        return result
    if concrete_str[1] == 3:
        cur = concrete_str[3]
        length = random.randint(7, 15)  # генерируем длину пароля
        cur = cur.replace("#N1", str(length))  # меняем длину пароля
        additional_info = random.randint(18,27)  # генерируем память под доп.сведения
        cur = cur.replace("#N2", str(additional_info))
        users = random.randint(15, 35)
        cur = cur.replace("#N3", str(users))
        answer = exc13_3(length, additional_info, users)
        result = [cur, answer]
        return result


def exc13_1(length, users, memory):
    result = int(memory / users - round((5*length)/8))
    return str(result)

def exc13_2(length, number, memory):
    result = int(memory - round(7 * length) / 8 - math.log(number, 2))
    return str(result)

def exc13_3(length, additional_info, users):
    result = int((round(length * 3 / 8) + additional_info) * users)
    return str(result)