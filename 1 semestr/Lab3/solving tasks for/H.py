# H
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
m = 0
for x in range(0, 1000+1, 1):
    if x - e != 0:
        if (a * x ** 3 + b * x ** 2 + c * x + d) / (x-e) == 0:
            m += 1
print(m)