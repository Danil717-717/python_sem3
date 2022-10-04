#  2. Напишите программу, которая найдёт произведение 
#  пар чисел списка. Парой считаем первый и последний 
#  элемент, второй и предпоследний и т.д.
#  in 4  out  [2, 5, 8, 10]    [20, 40]
#  in 5  out  [2, 2, 4, 8, 8]  [16, 16, 4]

import random

num = int(input())
num_list = random.sample(range(0, 40), num)
print(num_list)

def product_pairs(num_list):
    if num_list % 2 == 0:
        for i in range(num_list):
           num_list[i] * num_list[i - 1]
            