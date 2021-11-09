# B
#-*- coding: utf-8 -*-
a = []
n = int(input('кол-во необходимых чисел'))
for i in range(1, n+1):
    a1 = int(input())
    a.append(a1)
for i in range(0, n):
    if a[i] == 0:
        a.remove(a[i])
        a.append(0)
print(a)