import random

def text(concrete_str):
    if concrete_str[1] == 1:  # первый тип
        cur = concrete_str[3]
        ss = random.randint(2, 7)  # генерируем основание системы счисления
        cur = cur.replace("#N8", str(ss))  # меняем основание системы счисления
        if ss == 2 or ss == 3:  # если основание сс такое, то можем возводить в большую степень
            power1 = random.randint(1, 3)  # нижняя степень (не видна для пользователя)
        else:
            power1 = random.randint(1, 2)
        cur = cur.replace("#N1", str(ss**power1))  # последовательно заменяем числа в задании
        power2 = random.randint(1, 2)
        cur = cur.replace("#N6", str(ss ** power2))
        cur = cur.replace("#N7", str(ss))
        number1 = random.randint(300, 2018)  # верхняя степень (видна для пользователя)
        cur = cur.replace("#N2", str(number1))
        number2 = random.randint(300, 2018)
        cur = cur.replace("#N3", str(number2))
        while True:  # генерим число 3, пока не добьемся выполнения условия
            number3 = random.randint(300, 1000)
            if number3 < number2 or number3 < number1:
                break
        cur = cur.replace("#N4", str(number3))
        cur = cur.replace("#N5", str(ss - 1))

        answer = exc16_1(ss, number1, number2, number3, power1, power2)
        result = [cur, answer]
        return result
    if concrete_str[1] == 2:
        cur = concrete_str[3]
        ss = random.randint(2, 7)
        cur = cur.replace("#N8", str(ss))
        if ss == 2 or ss == 3:
            power1 = random.randint(1, 3)
        else:
            power1 = random.randint(1, 2)
        cur = cur.replace("#N1", str(ss**power1))
        power2 = random.randint(1, 2)
        cur = cur.replace("#N6", str(ss ** power2))
        number1 = random.randint(300, 2018)
        cur = cur.replace("#N2", str(number1))
        number2 = random.randint(300, 2018)
        cur = cur.replace("#N3", str(number2))
        number3 = random.randint(1, 65)  # генерируем число которое не представимо в виде основания сс в степени
        cur = cur.replace("#N4", str(number3))
        cur = cur.replace("#N5", str(ss - 1))
        answer = exc16_2(ss, number1, number2, number3, power1, power2)
        result = [cur, answer]
        return result


def exc16_1(ss, number1, number2, number3, power1, power2):  # решает первый тип
    tmp = (ss**power1)**number1 + (ss**power2)**number2 - ss**number3  # считаем ответ в десятичной
    tmp = str(from10toX(tmp, ss))  # перводим в нужную систему
    return str(tmp.count(str(ss-1)))  # считаем кол-во вхождений нужного числа

def exc16_2(ss, number1, number2, number3, power1, power2):
    tmp = (ss**power1)**number1 + (ss**power2)**number2 - number3
    tmp = str(from10toX(tmp, ss))
    return str(tmp.count(str(ss-1)))


def from10toX(number, ss):
    result = 0
    count = 0
    while number != 0:
        result += (number % ss) * 10 ** count
        number //= ss
        count += 1
    return result