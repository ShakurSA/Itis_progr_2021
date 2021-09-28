# J
a1, b1 = int(input()), int(input())
a2, b2 = int(input()), int(input())
c = a1 - a2
d = b1 - b2
if (c == d) or (c % 2 == 0 and d % 2 == 0) or (c % 2 == 1 and d % 2 == 1):
    print('YES')
else:
    print('NO')