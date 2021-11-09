# -*- coding: utf-8 -*-
n = int(input())

s = {}  # словарь ребенок родитель


for _ in range(1, n):  # читаем строки
    line = raw_input()
    child, parent = line.split()  
    s[child] = parent  

# guys = множество всех людей
guys = set(s.keys()) | set(s.values())  # имена = родители + дети

heights = {}  # предок поколение


# вычисляем поколение
def f(name):  
    if name not in s:  # если нет родителя
        heights[name] = 0  
        return 0  
    parent = s[name]  
    if parent in heights:  # если известно поколение родителя
        value = heights[parent] + 1  
    else:
        value = f(
            parent) + 1  
    heights[name] = value  # добавим в словарь heights нового предка 
    return value  


# предок=поколение
for name in guys:  
    if name not in heights:  # берём только тех, кого нет в словаре 
        f(name)  

for name in sorted(heights):
    print(name, heights[name])