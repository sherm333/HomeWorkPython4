'''
Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

*Пример*

- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]
'''

lst = [int(i) for i in input(('Введите список чисел через пробел:')).split()]
for i in lst:
   if lst.count(i) == 1:
       print(i)