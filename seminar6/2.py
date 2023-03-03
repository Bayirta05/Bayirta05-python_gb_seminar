'''Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному
диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)'''
import random
arr = []
res = []
n = int(input())
mn = int(input())
mx = int(input())
for i in range(n):
    a = random.randint(0, n)
    arr.append(a)
print(arr)
for i in range(len(arr)):
    if arr[i] > mn and arr[i] < mx:
        el = i
        res.append(el)
print(res)