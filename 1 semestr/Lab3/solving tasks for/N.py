# N
n = int(input())
summa = 0
for i in range(1, n + 1):
    summa += i
for i in range(n - 1):
    summa -= int(input())
print(summa)
