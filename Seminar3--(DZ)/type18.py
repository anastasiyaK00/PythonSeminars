#Задача 18: Требуется найти в массиве A[1..N] 
#самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N
# – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. 
#Последняя строка содержит число X
#*Пример:*
#5
#    1 2 3 4 5
#    6
#    -> 5

import random
n = int(input('Введите N - длину массива:'))
arr = []
arr = [random.randint(1, 10) for _ in range(n)]
print(arr)
x = int(input('Введите X - число к которому будет искать близкое по значению: '))
print(x,'к этому числу будем искать ближайшее')
arr = list(set(arr))
print(arr)
i=1
for i in range (len(arr) - 1):
    if arr[i]+x < arr[i+1]+x:
        bliz = arr[i]
        i=i+1
print (bliz)    

for i in range (len(arr) - 1):
    if x -arr[i] > x -arr[i+1]:
        bliz2 = arr[i]
        i=i+1
print (bliz2)    
