import random

def text(concrete_str):  # принимает конкретную строку из бд, возвращает задание и ответ
    if concrete_str[1] == 1:  # Первый тип
        cur = concrete_str[3]  # Выбираем текст задания
        number = random.randint(77, 256)
        cur = cur.replace("#N1", str(number))  # Заменяем параметр на определенное сгенерированное число
        answer = exc1_1(number)  # Вызываем функцию, которая вызывает ответ на первый тип в виде str
        result = [cur, answer]
        return result
    elif concrete_str[1] == 2:  # Второй тип
        cur = concrete_str[3]
        number = random.randint(77, 256)
        cur = cur.replace("#N1", str(number))
        answer = exc1_2(number)
        result = [cur, answer]
        return result
    elif concrete_str[1] == 3:
        cur = concrete_str[3]
        number1 = random.randint(50, 256)
        cur = cur.replace("#N1", str(from10to2(number1)))
        while True:
            number2 = random.randint(50, 256)
            if number1 < number2:
                break
        cur = cur.replace("#N2", str(from10to8(number2)))
        answer = exc1_3(number1, number2)
        result = [cur, answer]
        return result
    elif concrete_str[1] == 4:
        cur = concrete_str[3]
        number1 = random.randint(50, 255)
        cur = cur.replace("#N1", str(from10to8(number1)))
        while True:
            number2 = random.randint(50, 255)
            if number1 < number2:
                break
        cur = cur.replace("#N2", str(from10to16(number2)))
        answer = exc1_4(number1, number2)
        result = [cur, answer]
        return result
    elif concrete_str[1] == 5:
        cur = concrete_str[3]
        number1 = random.randint(50, 256)
        cur = cur.replace("#N1", str(from10to2(number1)))
        while True:
            number2 = random.randint(50, 256)
            if number1 < number2:
                break
        cur = cur.replace("#N2", str(from10to2(number2)))
        answer = exc1_5(number1, number2)
        result = [cur, answer]
        return result
    elif concrete_str[1] == 6:
        cur = concrete_str[3]
        number1 = random.randint(50, 256)
        cur = cur.replace("#N1", str(from10to16(number1)))
        while True:
            number2 = random.randint(50, 256)
            if number1 < number2:
                break
        cur = cur.replace("#N2", str(from10to16(number2)))
        answer = exc1_4(number1, number2)
        result = [cur, answer]
        return result
    elif concrete_str[1] == 7:
        cur = concrete_str[3]
        number1 = random.randint(50, 256)
        cur = cur.replace("#N1", str(from10to2(number1)))
        number2 = random.randint(50, 256)
        cur = cur.replace("#N2", str(from10to5(number2)))
        number3 = random.randint(50, 256)
        cur = cur.replace("#N3", str(from10to8(number3)))
        answer = exc1_7(number1, number2, number3)
        result = [cur, answer]
        return result
    else:
        return "oops. not found"


def from2to10(n):
    count = 0
    result = 0
    while n != 0:
        result += (2 ** count) * (n % 2)
        n //= 2
        count += 1
    return result


def from8to10(n):
    count = 0
    result = 0
    while n != 0:
        result += (8 ** count) * (n % 8)
        n //= 8
        count += 1
    return result


def from10to2(n):
    result = 0
    count = 0
    while n != 0:
        result += (n % 2) * 10 ** count
        n //= 2
        count += 1
    return result

def from10to5(n):
    result = 0
    count = 0
    while n != 0:
        result += (n % 5) * 10 ** count
        n //= 5
        count += 1
    return result


def from10to8(n):
    result = 0
    count = 0
    while n != 0:
        result += (n % 8) * 10 ** count
        n //= 8
        count += 1
    return result

def from10to16(n):
    result = ["0", "0"]
    count = 0
    for i in range(2):
        current = n % 16
        if current >= 10:
            if current == 10:
                result[i] = "A"
            if current == 11:
                result[i] = "B"
            if current == 12:
                result[i] = "C"
            if current == 13:
                result[i] = "D"
            if current == 14:
                result[i] = "E"
            if current == 15:
                result[i] = "F"
        else:
            result[i] = str(current)
        n //= 16
    res = result[1] + result[0]
    return res

def exc1_1(n):
    count = 0
    while n != 0:
        if n % 2 == 1:
            count += 1
        n //= 2
    return str(count)


def exc1_2(n):
    count = 0
    while n != 0:
        if n % 2 == 0:
            count += 1
        n //= 2
    return str(count)


def exc1_3(n1, n2):
    return str(n2 - n1 + 1)

def exc1_4(n1, n2):
    return str(n2 - n1)

def exc1_5(n1, n2):
    return str(n2 - n1 - 1)

def exc1_7(n1, n2, n3):
    return str(n1 - n2 + n3)
