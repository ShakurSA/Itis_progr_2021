# G
a1, b1 = int(input()), int(input())
a2, b2 = int(input()), int(input())
c = a1-a2
d = b1-b2
if ((c > 1) or (c < -1)) or ((d > 1) or (d < -1)):
    print('NO')
else:
    print('YES')