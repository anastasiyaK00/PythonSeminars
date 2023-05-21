#Вы пользуетесь общественным транспортом? 
#Вероятно, вы расплачивались за проезд и получали билет с номером. 
#Счастливым билетом называют такой билет с шестизначным номером, 
#где сумма первых трех цифр равна сумме последних трех. 
#Т.е. билет с номером 385916 – счастливый, 
#т.к. 3+8+5=9+1+6. 
#Вам требуется написать программу, которая проверяет счастливость билета.
    #*Пример:*
#385916 -> yes
#23456 -> no

ticket = int(input('Введите шестизначный номер билета: '))

number6 = ticket % 10
number5 = ticket % 100//10
number4 = ticket % 1000//100
number3 = ticket % 10000//1000
number2 = ticket % 100000//10000
number1 = ticket % 1000000//100000
print(number6, number5, number4, number3, number2, number1)

if (number1 + number2 + number3) == (number4 + number5 + number6):
    print('о, вы счастливчик!')
else:
    print('нет, билет не счастливый')