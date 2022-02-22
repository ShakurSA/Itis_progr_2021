# F
n = int(input())
z = 0
x = '0'
for i in range(1, n+1):
    print(('*'*(n-z))+x+('*'*(n-z)))
    x += '00'
    z += 1
print('0' * (2*n+1))
z = n - 1
x = (2*n - 1)
for f in range(1, n+1):
    print(('*'*(n-z))+'0'*x+('*'*(n-z)))
    z -= 1
    x -= 2