import random

#def text(concrete_str):
#    if concrete_str[1] == 1:











def checker(a, b, c, string):
    if a == string or b == string or c == string:
        return 0
    if a.find(string) != 0 and b.find(string) != 0 and c.find(string) != 0:
        return string
    else:
        return -1


def exc5_1(a, b, c):
    string1 = '0'
    string2 = '1'
    while(checker(a, b, c, string1) == -1):
        
        string1 += '0'
 #       if(checker(a, b, c, string1) == -1)
