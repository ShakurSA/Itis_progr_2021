# E
#-*- coding: utf-8 -*-
a = {int(input()) for i in range(2)} #нач конечная станция
b = {int(input()) for i in range(2)}
for i in range(min(a), max(a)): #добавление станций, которые находятся между нач и конеч
    a.add(i+1)
for i in range(min(b), max(b)):
    b.add(i+1)
a = a & b #пересечение станций 
print(len(a)) #длина = кол-во
