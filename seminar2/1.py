'''Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые –
гербом.Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки
были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые
 нужно перевернуть

5 -> 1 0 1 1 0
2'''
n = int(input())
op = 0
o, r = 0, 0
for i in range(1, n+1):
    k = int(input())
    if k == 0:
        r +=1
    elif k == 1:
        o +=1
if r > o:
    print(o)
else:
    print(r)