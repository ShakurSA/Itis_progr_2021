# C
import math
n = int(input())
x = float(input())
summa = math.cos(x) + x
for i in range(2, n+1, 1):
    summa += x + math.cos(summa)
print(summa - x)