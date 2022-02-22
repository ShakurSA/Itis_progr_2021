# F
n = int(input())
x = float(input())
a = n
summa = 0
for i in range(n+1):
    y = float(input())
    for i in range(a):
        y *= x
    summa += y
    a -= 1
print(summa)