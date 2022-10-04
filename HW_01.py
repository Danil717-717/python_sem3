# 1. Задайте список, состоящий из произвольных чисел, 
#    количество задаёт пользователь.Напишите программу, 
#    которая найдёт сумму элементов списка,
#    стоящих на нечётных позициях(не индексах).
#  in 5  out [10, 2, 3, 8, 9]  22
#  in 4  out [4, 2, 4, 9]      8

#import random

#num = int(input())
#num_list = random.sample(range(0, 40), num)
#print(num_list)

#s = sum(num_list[::2])       
#print(s)

#####################################

from random import sample

def list_nums(count: int):
    if count < 0:
        print("Ввели отрцатльное число")
        return []

    list_nums = sample(range(1, count * 2), count)
    return list_nums


def sum_elements(list_nums: list):
    sum_nums = 0
    for i in range(0, len(list_nums), 2):
        sum_nums += list_nums[i]
    return sum_nums

all_list = list_nums(int(input("Введите колличество чисел: ")))
print(all_list)
print(sum_elements(all_list))                