 #Петя, Катя и Сережа делают из бумаги журавликов. 
#Вместе они сделали S журавликов. 
 #Сколько журавликов сделал каждый ребенок, если известно, 
#что Петя и Сережа сделали одинаковое количество журавликов, 
#а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
       #*Пример:*
   #6 -> 1  4  1
   #24 -> 4  16  4
   #60 -> 10  40  10

TotalZhuravliki = int(input('Введите количество журавликов, сделанных детьми: '))

Petya = TotalZhuravliki// 3 // 2
Katya = (Petya + Petya) * 2
print('Катя сделала:', Katya)
print('Петя сделал:', Petya)
print('Серега сделал:', Petya)

#НО НЕ РАБОТАЕТ С 4... Т.Е. если петек и серега сделали по 1, то катя 2, но не работает:((())