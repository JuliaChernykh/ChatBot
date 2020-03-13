def from2to10(N):
    count = 0
    result = 0
    while N != 0:
        result += (2**count) * (N % 2)
        N //= 2
        count += 1
    return result

def from8to10(N):
    count = 0
    result = 0
    while N != 0:
        result += (8**count) * (N % 8)
        N //= 8
        count += 1
    return result

def exc1_1(N):
    count = 0
    while N != 0:
        if N % 2 == 1:
            count += 1
        N //= 2
    return count

def exc1_2(N):
    count = 0
    while N != 0:
        if N % 2 == 0:
            count += 1
        N //= 2
    return count
