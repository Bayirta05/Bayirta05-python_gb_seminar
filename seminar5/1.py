'''Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в
целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8'''

A = int(input())
B = int(input())
res = 0
for i in range(A):
    if B == 1:
        res = A
    elif B == 0:
        res = 1
    else:
        res = A * A**(B-1)
print(res)