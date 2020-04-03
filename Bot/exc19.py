import random
import math

def text(concrete_str):
    if concrete_str[1] == 1:  # первый тип
        cur = concrete_str[3]
        N = []
        for i in range(10):
            N.append(random.randint(0, 15))
        for i in range(10):
            cur = cur.replace("#N" + str(i), str(N[i]))
        answer = exc19_1(N)
        result = [cur, answer]
        return result
    if concrete_str[1] == 2:
        cur = concrete_str[3]
        N = []
        for i in range(10):
            N.append(random.randint(0, 15))
        for i in range(10):
            cur = cur.replace("#N" + str(i), str(N[i]))
        answer = exc19_2(N)
        result = [cur, answer]
        return result
    if concrete_str[1] == 3:
        cur = concrete_str[3]
        N = []
        for i in range(10):
            N.append(random.randint(0, 18))
        for i in range(10):
            cur = cur.replace("#N" + str(i), str(N[i]))
        answer = exc19_3(N)
        result = [cur, answer]
        return result
    if concrete_str[1] == 4:
        cur = concrete_str[3]
        N = []
        for i in range(10):
            N.append(random.randint(0, 10))
        for i in range(10):
            cur = cur.replace("#N" + str(i), str(N[i]))
        answer = exc19_4(N)
        result = [cur, answer]
        return result
    if concrete_str[1] == 5:
        cur = concrete_str[3]
        N = []
        for i in range(10):
            N.append(random.randint(0, 10))
        for i in range(10):
            cur = cur.replace("#N" + str(i), str(N[i]))
        answer = exc19_5(N)
        result = [cur, answer]
        return result
    if concrete_str[1] == 6:
        cur = concrete_str[3]
        N = []
        for i in range(11):
            N.append(random.randint(0, 25))
        for i in range(11):
            cur = cur.replace("#N0" + str(i), str(N[i]))
        cur = cur.replace("#N10", str(N[10]))
        answer = exc19_6(N)
        result = [cur, answer]
        return result
    if concrete_str[1] == 7:
        cur = concrete_str[3]
        N = []
        for i in range(10):
            N.append(random.randint(0, 25))
        for i in range(10):
            cur = cur.replace("#N" + str(i), str(N[i]))
        answer = exc19_7(N)
        result = [cur, answer]
        return result



def exc19_1(N):
    s = 0
    for j in range(9):
        if N[j] > N[j + 1]:
            s = s + 1
            t = N[j]
            N[j] = N[j + 1]
            N[j + 1] = t
    return str(s)

def exc19_2(N):
    c = 0
    for i in range(1, 10):
        if N[i] < N[0]:
            c = c + 1
            t = N[i]
            N[i] = N[0]
            N[0] = t
    return str(c)

def exc19_3(N):
    n = 10
    s = 0
    for i in range(1, n):
        if N[i - 1] < N[i]:
            N[i] = N[i] + N[i - 1]
            s = s + N[i]
    return str(s)

def exc19_4(N):
    n = 10
    s = 0
    for i in range(1, n):
        if N[i - 1] > 2 * N[i]:
            N[i] = 2 * N[i]
            s = s + N[i]
    return str(s)

def exc19_5(N):
    s = 0
    for i in range(0, 9):
        if N[i] < N[i + 1]:
            N[i + 1] -= N[i]
        else:
            N[i] -= N[i + 1]
        s += N[i]
    return str(s)

def exc19_6(N):
    s = 0
    n = 10
    for i in range(1, n + 1):
        s = s + N[i] - N[i - 1]
    return str(s)

def exc19_7(N):
    s = 0
    n = 10
    for i in range(2, n):
        s = s + N[i] - N[i - 2]
    return str(s)