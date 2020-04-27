import random
from random import choice


def text(concrete_str):  # принимает конкретную строку из бд, возвращает задание и ответ
    if concrete_str[1] == 1:  # Первый тип
        ans = []
        possible_codes = []
        generator('', possible_codes, 3)
        while (len(ans) == 0):
            codes = []
            for i in range(4):
                codes.append(choice(possible_codes))
            # codes = ['000', '001', '010', '11']  # наборы занятых кодов
            m_length = max(len(i) for i in codes)
            var = []
            ans = []
            generator('', var, m_length)
            for i in var:
                for j in var:
                    tmp = [k for k in codes]
                    tmp.append(i)
                    tmp.append(j)
                    if fano(tmp):
                        ans.append(i)
        if len(ans) != 0:
            mins = min(len(i) for i in ans)
            ans = [i for i in ans if len(i) == mins]
            mins = min(int(i) for i in ans)
            ans = [i for i in ans if int(i) == mins]
        cur = concrete_str[3]  # Выбираем текст задания
        for i in range(4):
            cur = cur.replace('#N' + str(i + 1), codes[i])
        result = [cur, str(ans[0])]
        return result
    elif concrete_str[1] == 2:
        ans = set()
        possible_codes = []
        generator('', possible_codes, 1)
        while (len(ans) < 2):
            codes = []
            for i in range(2):
                codes.append(choice(possible_codes))
            m_length = 3
            var = []
            ans = set()
            generator('', var, m_length)
            for i in var:
                for j in var:
                    tmp = [k for k in codes]
                    tmp.append(i)
                    tmp.append(j)
                    if fano(tmp):
                        ans.add(i)
        if len(ans) >= 2:
            ans = [i for i in ans]
            ans.sort(key=len)
            answer = len(codes[0]) + len(codes[1]) + len(ans[0]) + len(ans[1])
        cur = concrete_str[3]  # Выбираем текст задания
        for i in range(2):
            cur = cur.replace('#N' + str(i + 1), codes[i])
        result = [cur, str(answer)]
        return result
    elif concrete_str[1] == 3:
        ans = set()
        possible_codes = []
        generator('', possible_codes, 1)
        while (len(ans) < 3):
            codes = []
            for i in range(2):
                codes.append(choice(possible_codes))
            m_length = 3
            var = []
            ans = set()
            generator('', var, m_length)
            for i in var:
                for j in var:
                    for z in var:
                        tmp = [k for k in codes]
                        tmp.append(i)
                        tmp.append(j)
                        tmp.append(z)
                        if fano(tmp):
                            ans.add(i)
        if len(ans) >= 3:
            ans = [i for i in ans]
            ans.sort(key=len)
            answer = len(codes[0]) + len(codes[1]) + len(ans[0]) + len(ans[1]) + len(ans[2])
        cur = concrete_str[3]  # Выбираем текст задания
        for i in range(2):
            cur = cur.replace('#N' + str(i + 1), codes[i])
        result = [cur, str(answer)]
        return result


def generator(s, a, m_length):  # генерит все возможные варианты строк до размера max_length + 1 и append'ит в a
    if len(s) <= m_length + 1:
        if s != '':
            a.append(s)
        generator(s + '0', a, m_length)
        generator(s + '1', a, m_length)


def fano(codes):  # возвращает 1, если выполняется условие Фано
    length = len(codes)
    for i in range(length):
        for j in range(i + 1, length):
            if codes[i] == codes[j][0:len(codes[i])] or codes[j] == codes[i][0:len(codes[j])]:
                return 0
    return 1