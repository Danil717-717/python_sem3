# 2. Задайте список, состоящий из произвольных слов, количество 
#    задаёт пользователь. Напишите программу, которая 
#    определит индекс второго вхождения строки в списке
#    либо сообщит, что её нет.
#   in 6 >> out ['xzy','yxz','xxz','xzy','yzz','xzy']  >> in xzy >> out 3
#   in 6 >> out ['xzy','yxz','xxz','xzy','yzz','xzy']  >> in yxz >> out -1

from random import choices

def  collects (count, b):
    len = []
    for i in range(count):
        y = choices(b, k = 3)     # сформировали список из 3 элементов, k - встроенный параметр choices
        len.append("".join(y))    # склеили список
    return len
my_list = collects(8, "abc")
print(my_list)    

             # покозали что spisok в формате
def find(slovo, spisok: list):              # find(искомое слово, список слов)
    if slovo in spisok and spisok.count(slovo) > 1:  #  1 проверка есть ли это слово в списке and сколько
        p = spisok.index(slovo)                      # слово раз повторяется в списке
        print(spisok.index(slovo, p + 1))  
    else:
        print(-1)

find(input(), my_list)        


