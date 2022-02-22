# F
#-*- coding: utf-8 -*-
N, K = [int(s) for s in raw_input().split()]
Rabochie = set([s for s in range(1, N + 1) if s % 7 not in (6, 0)]) #находим только рабочие дни
poryadok = set(Rabochie)
for l in range(K):
    a, b = [int(s) for s in raw_input().split()] #находим в какие дни не было забастовок
    maxx = (N - a) // b + 1
    poryadok -= {a + b*i for i in range(maxx)}
print(len(Rabochie) - len(poryadok)) #из кол-ва рабочих вычитаем кол-во спокойных дней и находим кол-во забастовок
