# E
import math
n = int(input())
s = 0
for m in range(1, n+1, 1):
    s += ((math.factorial(m-1)) ** 2) / (math.factorial(2*m))
print(s)