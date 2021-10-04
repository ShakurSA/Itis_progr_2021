# P
F0 = 0
F1 = 1
n = int(input())
summa = 0
x = 1
if n == 1:
    print(1)
if n == 0:
    print(0)
while x < n:
    summa = F0 + F1
    F0 = F1
    F1 = summa
    x += 1
print(summa)