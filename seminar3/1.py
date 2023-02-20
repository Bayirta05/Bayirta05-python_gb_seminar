'''Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

пример
5
1 2 3 4 5
3
-> 1'''

'''N = int(input())
A = []
count = 0
for i in range(N):
    i = int(input())
    A.append(i)
print(A)
X = int(input())
for i in range(len(A)):
    if A[i] == X:
        count += 1
print(count)'''

N = int(input())
A = [int(input()) for i in range(N)]
count = 0
print(A)
X = int(input())
for i in range(len(A)):
    if A[i] == X:
        count += 1
print(count)