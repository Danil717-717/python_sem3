# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.
#    in 4  >> out [7, 9, 2, 3]  >> 9
#    in 5  >> out [2, 5 ,2, 7, 9]  >> 13

from random import sample

def find_num(num, q):
    q = q if q >0 else -q
    arr = sample(range(1, q * 2), q)  # sample выбирает из вложенного в него
    print(arr)                        # то что мы ему передаем
    if num in arr:
        return True
    return False    

print(find_num(-50, -10))  


############################################

def find_num(count, num):
    if count < 0:
        return "Negative value of the number of numbers!"

    list_nums = sample(range(1, count * 2), count)
    print(list_nums)

    if num in list_nums:
        return f"The number - {num} is present in the list."
    return f"The number - {num} is not in the list."


print(find_num(int(input("Number of numbers: ")), int(input("Number: "))))
