# 5. ** Задайте число. Составьте список чисел Фибоначчи,
#       в том числе для отрицательных индексов.
#  in 3  >> out 2 -1 1 0 1 1 2
#  in 8  >> out -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

def neg_fib(num: int):
    a, b = 1, 1
    list_nums = [0]

    for i in range(num):
        list_nums.append(a)
        list_nums.insert(0, a * (-1) ** i)
        a, b = b, b + a

    return list_nums


print(*neg_fib(int(input())))