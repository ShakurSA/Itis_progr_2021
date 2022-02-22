# B
n = int(input())
x = int(input())
summa = 0
for i in range(n+1):
    a = int(input())
    summa += a * x ** (n-i)
print(summa)