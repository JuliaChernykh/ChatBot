import random
import math

def text(concrete_str):  # принимает конкретную строку из бд, возвращает задание и ответ
    if concrete_str[1] == 1:  # Первый тип
        cur = concrete_str[3]  # Выбираем текст задания
        powers = []
        for i in range(7, 12):
            powers.append(2**i)
        for i in range(4, 8):
            powers.append((2**i)*10)
        firstsize = random.choice(powers)  # Генерируем разрешние
        secondsize = random.choice(powers)  # Генерируем разрешние
        print(firstsize, secondsize)
        cur = cur.replace("#N1", str(firstsize))
        cur = cur.replace("#N2", str(secondsize))
        colors = []
        for i in range(4, 11):
            colors.append(2**i)
        numberofcolors = random.choice(colors)  # Генерируем количество цветов для задания
        cur = cur.replace("#N3", str(numberofcolors))
        answer = exc9_1(firstsize, secondsize, numberofcolors)  # Вызываем функцию, которая возвращает ответ в виде str
        result = [cur, answer]
        return result
    if concrete_str[1] == 2:
        cur = concrete_str[3]  # Выбираем текст задания
        powers = []
        for i in range(7, 12):
            powers.append(2**i)
        for i in range(4, 8):
            powers.append((2**i)*10)
        firstsize = random.choice(powers)  # Генерируем разрешние
        secondsize = random.choice(powers)  # Генерируем разрешние
        print(firstsize, secondsize)
        cur = cur.replace("#N1", str(firstsize))
        cur = cur.replace("#N2", str(secondsize))
        volume = random.choice(powers)
        while volume*1024*8 <= firstsize*secondsize:
            volume = random.choice(powers)  # Генерируем объем
        cur = cur.replace("#N3", str(volume))
        answer = exc9_2(firstsize, secondsize, volume)  # Вызываем функцию, которая возвращает ответ в виде str
        result = [cur, answer]
        return result
    if concrete_str[1] == 3:
        cur = concrete_str[3]  # Выбираем текст задания
        powerbefore = [10, 12, 14, 16, 18, 20, 22, 24]
        power1 = random.choice(powerbefore)  # Генерируем исходную глубину цвета
        cur = cur.replace("#N1", str(power1))
        powerafter = []
        for i in range(5, 13):
            powerafter.append(i)
        power2 = random.choice(powerafter)  # Генерируем глубину цвета после преобразования
        while power1 % power2 != 0 or power1 == power2:
            power2 = random.choice(powerafter)
        colors = 2**power2
        cur = cur.replace("#N3", str(colors))
        sizebefore = random.randint(10, 30)  # Генерируем изначальный размер файла
        while sizebefore % (power1 / power2) != 0:
            sizebefore = random.randint(10, 30)
        cur = cur.replace("#N2", str(sizebefore))
        answer = exc9_3(power1, power2, sizebefore)  # Вызываем функцию, которая возвращает ответ в виде str
        result = [cur, answer]
        return result
    if concrete_str[1] == 4:
        cur = concrete_str[3]  # Выбираем текст задания
        time = [10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 28, 30]
        timeXtoA = random.choice(time)  # Генерируем время передачи х в А
        cur = cur.replace("#N1", str(timeXtoA))
        sizeup = random.randint(2, 8)  # Генерируем изменение разрешения
        sizedown = random.randint(2, 8)  # Генерируем изменение частоты дискретизации
        speed = random.randint(2, 5)  # Генерируем, во сколько пр.сп. канала Б выше
        while sizeup == sizedown or (timeXtoA * sizeup) % sizedown != 0 or ((timeXtoA * sizeup) / sizedown) % speed != 0:
            sizeup = random.randint(2, 8)  # Генерируем изменение разрешения
            sizedown = random.randint(2, 8)  # Генерируем изменение частоты дискретизации
            speed = random.randint(2, 5)  # Генерируем, во сколько пр.сп. канала Б выше
        cur = cur.replace("#N2", str(sizeup))
        cur = cur.replace("#N3", str(sizedown))
        cur = cur.replace("#N4", str(speed))

        answer = exc9_4(timeXtoA, sizeup, sizedown, speed)  # Вызываем функцию, которая возвращает ответ в виде str
        result = [cur, answer]
        return result
    if concrete_str[1] == 5:
        cur = concrete_str[3]  # Выбираем текст задания
        canals = random.choice([2, 4])  # Генерируем количество каналов, затем меняем текст задачи
        if canals == 2:
            cur = cur.replace("#N1", 'двух')
            cur = cur.replace("#N2", 'стерео')
        if canals == 4:
            cur = cur.replace("#N1", 'четырёх')
            cur = cur.replace("#N2", 'квадро')
        numbers = [16, 24, 32, 48, 64, 72]
        resolution = random.choice(numbers)  # Генерируем разрешение
        frequency = random.choice(numbers)  # Генерируем частоту дискретизации
        numbers[0] = 60
        numbers[1] = 70
        numbers.append(50)
        size = random.choice(numbers)  # Генерируем размер
        cur = cur.replace("#N3", str(frequency))
        cur = cur.replace("#N4", str(resolution))
        cur = cur.replace("#N5", str(size))
        answer = exc9_5(canals, frequency, resolution, size)  # Вызываем функцию, которая возвращает ответ в виде str
        result = [cur, answer]
        return result
    if concrete_str[1] == 6:
        cur = concrete_str[3]  # Выбираем текст задания
        canals = random.choice([1, 2, 4])  # Генерируем количество каналов, затем меняем текст задачи
        if canals == 1:
            cur = cur.replace("#N1", 'одно')
            cur = cur.replace("#N2", 'моно')
        if canals == 2:
            cur = cur.replace("#N1", 'двух')
            cur = cur.replace("#N2", 'стерео')
        if canals == 4:
            cur = cur.replace("#N1", 'четырёх')
            cur = cur.replace("#N2", 'квадро')
        numbers = [16, 24, 32, 48, 64, 72]
        resolution = random.choice(numbers)  # Генерируем разрешение
        frequency = random.choice(numbers)  # Генерируем частоту дискретизации
        time = random.randint(2, 4)  # Генерируем время записи
        cur = cur.replace("#N3", str(frequency))
        cur = cur.replace("#N4", str(resolution))
        cur = cur.replace("#N5", str(time))
        answer = exc9_6(canals, frequency, resolution, time)  # Вызываем функцию, которая возвращает ответ в виде str
        result = [cur, answer]
        return result

def exc9_1(firstsize, secondsize, numberofcolors):
    result = int((firstsize * secondsize * math.log(numberofcolors, 2)) / (2**3 * 2**10))
    return str(result)

def exc9_2(firstsize, secondsize, volume):
    result = int((volume * 1024 * 8) / (firstsize * secondsize))
    return str(result)

def exc9_3(power1, power2, sizebefore):
    result = int(sizebefore / (power1 / power2))
    return str(result)

def exc9_4(timeXtoA, sizeup, sizedown, speed):
    result = int(((timeXtoA * sizeup) / sizedown) / speed)
    return str(result)

def exc9_5(canals, frequency, resolution, size):
    result = round(size*1024*1024*8 / (canals*frequency*1000*resolution*60))
    return str(result)

def exc9_6(canals, frequency, resolution, time):
    result = (canals * frequency*1000 * resolution * time*60) / (1024*1024*8)
    return str(int(5 * round(float(result) / 5)))