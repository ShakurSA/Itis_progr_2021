# A
n = int(input())
x = 1
while x <= n:
    if (x ** 0.5) % 1 == 0:
        print(x)
    x += 1