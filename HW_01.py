# 1. Задайте список, состоящий из произвольных чисел, 
#    количество задаёт пользователь.Напишите программу, 
#    которая найдёт сумму элементов списка,
#    стоящих на нечётных позициях(не индексах).
#  in 5  out [10, 2, 3, 8, 9]  22
#  in 4  out [4, 2, 4, 9]      8

import random

num = int(input())
num_list = random.sample(range(0, 40), num)
print(num_list)

s = sum(num_list[::2])       
print(s)