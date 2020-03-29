import random

def text(concrete_str):  # принимает конкретную строку из бд, возвращает задание и ответ
    if concrete_str[1] == 1:  # Первый тип
        ans = []
        a = [[random.randint(0, 2) for i in range(4)] for i in range(3)]  # Матрица из нулей и единиц
        f = random.randint(0, 1)  # Значение функции
        rand = random.randint(0, 1)  # Выбирает выражение
        ans = solver(a, f, rand)  # Вызываем функцию, которая вызывает ответ на первый тип в виде str
        while len(ans) != 1:
            # Подбираем параметры до тех пор, пока не находим условия, которые имеют один вариант решения задачи
            a = [[random.randint(0, 2) for i in range(4)] for i in range(3)]
            f = random.randint(0, 1)
            rand = random.randint(0, 1)
            ans = solver(a, f, rand)
        cur = concrete_str[3]  # Выбираем текст задания
        cur = cur.replace("#N1", textexp(rand))  # Заменяем параметр на определенное сгенерированное число
        for i in range(3):
            for j in range(4):
                if a[i][j] == 2:
                    cur = cur.replace("#A" + str(i) + str(j), '_')
                else:
                    cur = cur.replace("#A" + str(i) + str(j), str(a[i][j]))
        cur = cur.replace("#N2", str(f))
        result = [cur, ans[0]]
        return result


def textexp(rand):  # Возвращает текст задания, принимает номер задания
    # →
    if rand == 0:
        return '(x ∧ y) ∨ (y ≡ z) ∨ w'
    elif rand == 1:
        return '(x ∧ y) ∧ (y ≡ z) ∨ w'
    else:
        return 'error'


def expression(x, y, z, w, f, rand):  # Проверяет выражение на условие в зависимости от переменной rand
    if rand == 0:
        if ((x and y) or (y == z) or w) == f:
            return 1
        else:
            return 0
    if rand == 1:
        if (((x and y) and (y == z)) or w) == f:
            return 1
        else:
            return 0


def checker(x, y, z, w, f, rand):  # Проверяет, подходит ли такое решение
    if x == 2:
        return checker(0, y, z, w, f, rand) or checker(1, y, z, w, f, rand)
    elif y == 2:
        return checker(x, 0, z, w, f, rand) or checker(x, 1, z, w, f, rand)
    elif z == 2:
        return checker(x, y, 0, w, f, rand) or checker(x, y, 1, w, f, rand)
    elif w == 2:
        return checker(x, y, z, 0, f, rand) or checker(x, y, z, 1, f, rand)
    elif expression(x, y, z, w, f, rand):
        return 1
    else:
        return 0


def solver(a, f, rand):  # Проверяет все возможные перестановки x, y, z и w
    ans = []
    if (checker(a[0][0], a[0][1], a[0][2], a[0][3], f, rand) and
            checker(a[1][0], a[1][1], a[1][2], a[1][3], f, rand) and
            checker(a[2][0], a[2][1], a[2][2], a[2][3], f, rand)):
        ans.append('xyzw')
    if (checker(a[0][0], a[0][1], a[0][3], a[0][2], f, rand) and
            checker(a[1][0], a[1][1], a[1][3], a[1][2], f, rand) and
            checker(a[2][0], a[2][1], a[2][3], a[2][2], f, rand)):
        ans.append('xywz')
    if (checker(a[0][0], a[0][2], a[0][1], a[0][3], f, rand) and
            checker(a[1][0], a[1][2], a[1][1], a[1][3], f, rand) and
            checker(a[2][0], a[2][2], a[2][1], a[2][3], f, rand)):
        ans.append('xzyw')
    if (checker(a[0][0], a[0][2], a[0][3], a[0][1], f, rand) and
            checker(a[1][0], a[1][2], a[1][3], a[1][1], f, rand) and
            checker(a[2][0], a[2][2], a[2][3], a[2][1], f, rand)):
        ans.append('xzwy')
    if (checker(a[0][0], a[0][3], a[0][1], a[0][2], f, rand) and
            checker(a[1][0], a[1][3], a[1][1], a[1][2], f, rand) and
            checker(a[2][0], a[2][3], a[2][1], a[2][2], f, rand)):
        ans.append('xwyz')
    if (checker(a[0][0], a[0][3], a[0][2], a[0][1], f, rand) and
            checker(a[1][0], a[1][3], a[1][2], a[1][1], f, rand) and
            checker(a[2][0], a[2][3], a[2][2], a[2][1], f, rand)):
        ans.append('xwzy')

    ######################################################

    if (checker(a[0][1], a[0][0], a[0][2], a[0][3], f, rand) and
            checker(a[1][1], a[1][0], a[1][2], a[1][3], f, rand) and
            checker(a[2][1], a[2][0], a[2][2], a[2][3], f, rand)):
        ans.append('yxzw')
    if (checker(a[0][1], a[0][0], a[0][3], a[0][2], f, rand) and
            checker(a[1][1], a[1][0], a[1][3], a[1][2], f, rand) and
            checker(a[2][1], a[2][0], a[2][3], a[2][2], f, rand)):
        ans.append('yxwz')
    if (checker(a[0][1], a[0][2], a[0][0], a[0][3], f, rand) and
            checker(a[1][1], a[1][2], a[1][0], a[1][3], f, rand) and
            checker(a[2][1], a[2][2], a[2][0], a[2][3], f, rand)):
        ans.append('yzxw')
    if (checker(a[0][1], a[0][2], a[0][3], a[0][0], f, rand) and
            checker(a[1][1], a[1][2], a[1][3], a[1][0], f, rand) and
            checker(a[2][1], a[2][2], a[2][3], a[2][0], f, rand)):
        ans.append('yzwx')
    if (checker(a[0][1], a[0][3], a[0][0], a[0][2], f, rand) and
            checker(a[1][1], a[1][3], a[1][0], a[1][2], f, rand) and
            checker(a[2][1], a[2][3], a[2][0], a[2][2], f, rand)):
        ans.append('ywxz')
    if (checker(a[0][1], a[0][3], a[0][2], a[0][0], f, rand) and
            checker(a[1][1], a[1][3], a[1][2], a[1][0], f, rand) and
            checker(a[2][1], a[2][3], a[2][2], a[2][0], f, rand)):
        ans.append('ywzx')

    ######################################################

    if (checker(a[0][2], a[0][1], a[0][0], a[0][3], f, rand) and
            checker(a[1][2], a[1][1], a[1][0], a[1][3], f, rand) and
            checker(a[2][2], a[2][1], a[2][0], a[2][3], f, rand)):
        ans.append('zyxw')
    if (checker(a[0][2], a[0][1], a[0][3], a[0][0], f, rand) and
            checker(a[1][2], a[1][1], a[1][3], a[1][0], f, rand) and
            checker(a[2][2], a[2][1], a[2][3], a[2][0], f, rand)):
        ans.append('zywx')
    if (checker(a[0][2], a[0][0], a[0][1], a[0][3], f, rand) and
            checker(a[1][2], a[1][0], a[1][1], a[1][3], f, rand) and
            checker(a[2][2], a[2][0], a[2][1], a[2][3], f, rand)):
        ans.append('zxyw')
    if (checker(a[0][2], a[0][0], a[0][3], a[0][1], f, rand) and
            checker(a[1][2], a[1][0], a[1][3], a[1][1], f, rand) and
            checker(a[2][2], a[2][0], a[2][3], a[2][1], f, rand)):
        ans.append('zxwy')
    if (checker(a[0][2], a[0][3], a[0][1], a[0][0], f, rand) and
            checker(a[1][2], a[1][3], a[1][1], a[1][0], f, rand) and
            checker(a[2][2], a[2][3], a[2][1], a[2][0], f, rand)):
        ans.append('zwyx')
    if (checker(a[0][2], a[0][3], a[0][0], a[0][1], f, rand) and
            checker(a[1][2], a[1][3], a[1][0], a[1][1], f, rand) and
            checker(a[2][2], a[2][3], a[2][0], a[2][1], f, rand)):
        ans.append('zwxy')

    ######################################################

    if (checker(a[0][3], a[0][1], a[0][2], a[0][0], f, rand) and
            checker(a[1][3], a[1][1], a[1][2], a[1][0], f, rand) and
            checker(a[2][3], a[2][1], a[2][2], a[2][0], f, rand)):
        ans.append('wyzx')
    if (checker(a[0][3], a[0][1], a[0][0], a[0][2], f, rand) and
            checker(a[1][3], a[1][1], a[1][0], a[1][2], f, rand) and
            checker(a[2][3], a[2][1], a[2][0], a[2][2], f, rand)):
        ans.append('wyxz')
    if (checker(a[0][3], a[0][2], a[0][1], a[0][0], f, rand) and
            checker(a[1][3], a[1][2], a[1][1], a[1][0], f, rand) and
            checker(a[2][3], a[2][2], a[2][1], a[2][0], f, rand)):
        ans.append('wzyx')
    if (checker(a[0][3], a[0][2], a[0][0], a[0][1], f, rand) and
            checker(a[1][3], a[1][2], a[1][0], a[1][1], f, rand) and
            checker(a[2][3], a[2][2], a[2][0], a[2][1], f, rand)):
        ans.append('wzxy')
    if (checker(a[0][3], a[0][0], a[0][1], a[0][2], f, rand) and
            checker(a[1][3], a[1][0], a[1][1], a[1][2], f, rand) and
            checker(a[2][3], a[2][0], a[2][1], a[2][2], f, rand)):
        ans.append('wxyz')
    if (checker(a[0][3], a[0][0], a[0][2], a[0][1], f, rand) and
            checker(a[1][3], a[1][0], a[1][2], a[1][1], f, rand) and
            checker(a[2][3], a[2][0], a[2][2], a[2][1], f, rand)):
        ans.append('wxzy')
    return ans