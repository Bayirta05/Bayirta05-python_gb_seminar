'''Задача 2: Найдите сумму цифр трехзначного числа.
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
'''

N = int(input('Введите трехзначное число: '))
a = N % 10
b = (N // 10) % 10
c = N // 100
print(a + b + c)