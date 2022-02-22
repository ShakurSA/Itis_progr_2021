# I
# -*- coding: utf-8 -*-
d = {}
for i in range(int(input())):
    for slova in raw_input().split():
        d[slova] = d.get(slova, 0) + 1 #+ последнее значение суммы в словарь
for i in sorted(d.items(), key=lambda x: (-x[1], x[0])):
    print(i[0])