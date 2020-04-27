import random

def text(concrete_str):  # принимает конкретную строку из бд, возвращает задание и ответ
    if concrete_str[1] == 1:  # Первый тип
        cur = concrete_str[3]  # Выбираем текст задания
        number = random.randint(70, 135)  # Генерируем число
        cur = cur.replace("#N1", str(number))
        answer = exc6_1(number)  # Вызываем функцию, которая возвращает ответ в виде str
        result = [cur, answer]
        return result
    if concrete_str[1] == 2:
        cur = concrete_str[3]  # Выбираем текст задания
        number = random.randint(157, 245)  # Генерируем число
        cur = cur.replace("#N1", str(number))
        answer = exc6_2(number)  # Вызываем функцию, которая возвращает ответ в виде str
        result = [cur, answer]
        return result
    if concrete_str[1] == 3:
        cur = concrete_str[3]  # Выбираем текст задания
        number = random.randint(21, 201)  # Генерируем число
        cur = cur.replace("#N1", str(number))
        answer = exc6_3(number)  # Вызываем функцию, которая возвращает ответ в виде str
        result = [cur, answer]
        return result
    if concrete_str[1] == 4:
        cur = concrete_str[3]  # Выбираем текст задания
        number = 0
        while number % 2 == 0:
            number = random.randint(43, 177)  # Генерируем нечетное число
        cur = cur.replace("#N1", str(number))
        answer = exc6_4(number)  # Вызываем функцию, которая возвращает ответ в виде str
        result = [cur, answer]
        return result

def from10toX(number, ss):
    result = 0
    count = 0
    count_of_1 = 0
    count_of_0 = 0
    while number != 0:
        result += (number % ss) * 10 ** count
        number //= ss
        count += 1
    return result

def number_of_1(number):
    count_of_1 = 0
    while number != 0:
        if number % 2 == 1:
            count_of_1 += 1
        number //= 10
    return count_of_1

def from2to10(n):
    count = 0
    result = 0
    while n != 0:
        result += (2**count) * (n % 2)
        n //= 10
        count += 1
    return result

def algorithm_1(N):
    for i in range(2):
        curr = number_of_1(N)
        if curr % 2 == 0:
            N *= 10
        else:
            N = N*10 + 1
    return N

def exc6_1(number):
    R = from10toX(number, 2)
    N = R // 100
    while R != N:
        number += 1
        R = from10toX(number, 2)
        N = R // 100
        N = algorithm_1(N)
    print(N)
    N = from2to10(N)
    print(N)
    return str(N)

def exc6_2(number):
    number -= 1
    result = 255 - number
    return str(result)

def exc6_3(number):
    result = 256 - number
    return str(result)

def exc6_4(number):
    result = int((255 - number) / 2)
    return str(result)



