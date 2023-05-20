# Найдите сумму цифр трехзначного числа.
# Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input('Введите трехзначное число: '))

numberThree = number % 10
numberTwo = (number // 10) % 10
numberOne = (number // 100) % 10

print(numberThree, numberTwo, numberOne)

print('Сумма цифр числа', number, '=', numberOne+numberTwo+numberThree)
