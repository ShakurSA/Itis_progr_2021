# L
a1, b1 = int(input()), int(input())
a2, b2 = int(input()), int(input())
c = b1+(a2-a1)
d = b1-(a2-a1)
if (a2-a1 > 0) and (b2 < c) and (b2 > d) and (a2+b2 % 2 != 0):
    print('YES')
else:
    print('NO')