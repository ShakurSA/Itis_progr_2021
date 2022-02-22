# K
n = int(input())
s = 1
if n % 2 == 0:
    for i in range(2 ,n+1, 2):
        s *= i
if n % 2 != 0:
    for i in range(1, n+1, 2):
        s *= i
print(s)