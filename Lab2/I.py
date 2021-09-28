# I
a = int(input())
b = int(input())
c = b - a + 1
if (a - 1) % c == b % c == 0:
    print('YES')
else:
    print('NO')