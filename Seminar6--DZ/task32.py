'''Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)'''

import random
n = int(input('Введите N:'))
arr = []
arr = [random.randint(1,100) for _ in range(n)]
print(arr)

minim = int(input("Add min: "))
maxim = int(input("Add max: "))

for i in range(len(arr)):
    if minim < arr[i] < maxim:
        print(i)