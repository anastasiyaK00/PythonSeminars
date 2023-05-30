#Требуется вывести все целые степени двойки 
#(т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введите N: '))

stepeni = 1
a =0

while a < n :
    stepeni = stepeni * 2
    a = a+1
    print("Двойка в степени", a, "=", stepeni)
