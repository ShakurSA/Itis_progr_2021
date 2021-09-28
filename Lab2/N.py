# N
a = int(input())
b = int(input())
c = int(input())
x = 0
if a == b:
    x += 1
if a == c:
    x += 1
if b == c:
    x += 1
if x == 1:
    x += 1
print(x)