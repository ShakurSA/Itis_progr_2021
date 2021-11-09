# A
#-*- coding: utf-8 -*-
n = 8 #кол-во ферзей
a = []
b = []
flag = 0
for i in range(1,n+1):
    a1, b1 = [int(s) for s in raw_input().split()]  #запись координат
    a.append(a1) # в а первая координата всех верзей
    b.append(b1) # в б вторая координата
for i in range(n):
    for j in range(i+1,n):
        if a[i] == a[j] or b[i] == b[j] or abs(a[i] - a[j]) == abs(b[i] - b[j]): #условие на выполнение(лиюо по диагонали стоят, либо по одной линии)
            flag = 1
if flag == 1:
    print('YES')
if flag == 0:
    print('NO')