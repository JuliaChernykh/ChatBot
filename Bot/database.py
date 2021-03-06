import pandas as pd
import random
import exc1
import exc2
import exc5
import exc6
import exc9
import exc11
import exc13
import exc16
import exc19
data = pd.read_csv("DataBase.csv", header=None)

def random_exc(n):
    tmp = data[data[0] == n]  # Выбираем те строчки из базы данных, в которых номер задания совпадает с требуемым
    concrete_str = tmp.iloc[random.randint(0, len(tmp[0])-1), :]  # Рандомно выбираем строчку с нужным заданием
    if n == 1:
        return exc1.text(concrete_str.tolist())  # Вызываем функцию для первого задания
    elif n == 2:
        return exc2.text(concrete_str.tolist())
    elif n == 5:
        return exc5.text(concrete_str.tolist())
    elif n == 6:
        return exc6.text(concrete_str.tolist())
    elif n == 9:
        return exc9.text(concrete_str.tolist())
    elif n == 11:
        return exc11.text(concrete_str.tolist())
    elif n == 13:
        return exc13.text(concrete_str.tolist())
    elif n == 16:
        return exc16.text(concrete_str.tolist())
    elif n == 19:
        return exc19.text(concrete_str.tolist())