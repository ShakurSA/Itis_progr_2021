# U
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == 0 and b == 0:
    print('INF')
elif a == 0 or b*c == a*d:
    print('NO')
elif b % a == 0:
    x = -b // a
    print(x)
else:
    print('NO')