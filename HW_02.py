#  2. Напишите программу, которая найдёт произведение 
#  пар чисел списка. Парой считаем первый и последний 
#  элемент, второй и предпоследний и т.д.
#  in 4  out  [2, 5, 8, 10]    [20, 40]
#  in 5  out  [2, 2, 4, 8, 8]  [16, 16, 4]

from random import sample

def list_nums(count: int):
    if count < 0:
        print("Ввели отрцатльное число")
        return []

    list_nums = sample(range(1, count * 2), count)
    return list_nums 

def product_pairs(list_nums: list):
    new_list = []
    len_list = len(list_nums)

    for i in range(len_list // 2):
        new_list.append(list_nums[i] * list_nums[len_list - i - 1])

    if len_list % 2:
        new_list.append(list_nums[len_list // 2])
    return new_list

all_list = list_nums(int(input("Введите количество чисел: ")))
print(all_list)
print(product_pairs(all_list))            
            