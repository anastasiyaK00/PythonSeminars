def check_fib_position(num):
     # Инициализация начальных значений
    fib_prev = 0
    fib_curr = 1
    n = 2
# Вычисление чисел Фибоначчи
    while fib_curr < num:
        fib_next = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = fib_next
        n += 1

# Проверка и вывод результата
    if fib_curr == num:
        print("Число", num, "является", n, "-ым числом Фибоначчи")
    else:
        print("Число", num, "не является числом Фибоначчи и равно -1")
    return n

A = int(input("Введите число A: "))


print (check_fib_position(A))