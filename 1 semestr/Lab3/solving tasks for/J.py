# J
z = ''
for x in range (10, 100, 1):
    if (x % 10) * (x // 10) * 2 == x:
        z += str(x) + ' '
print(z)

