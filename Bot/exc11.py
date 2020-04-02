import random
import math


def text(concrete_str):  # принимает конкретную строку из бд, возвращает задание и ответ
    if concrete_str[1] == 1:  # Первый тип
        cur = concrete_str[3]  # Выбираем текст задания

        n = random.randint(5, 8)
        cur = cur.replace("#N1", str(n))
        a = random.randint(0, 2)
        cur = cur.replace("#N2", str(a))
        b = random.randint(1, 2)
        cur = cur.replace("#N3", str(b))
        c = random.randint(2, 3)
        cur = cur.replace("#N4", str(c))

        answer = exc11_1(n, a, b, c)  # Вызываем функцию, которая возвращает ответ в виде str
        result = [cur, answer]
        return result


def exc11_1(n, a, b, c):
    res = 0
    if n > a:
        exc11_1(n - b)
        print(n)
        res = res * 10 + n
        # result.append(n)
        exc11_1(n - c)
    return str(res)
