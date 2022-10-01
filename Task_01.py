# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.
#    in 4  >> out [7, 9, 2, 3]  >> 9
#    in 5  >> out [2, 5 ,2, 7, 9]  >> 13

from random import sample

def find_num(num, q):
    q = q if q >0 else -q
    arr = sample(range(1, q * 2), q)
    print(arr)
    if num in arr:
        return True
    return False    

print(find_num(-50, -10))    
