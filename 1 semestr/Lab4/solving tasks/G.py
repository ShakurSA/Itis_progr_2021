# G
n = int(input())
z = 1
x = 2*n-1
for i in range(1,n+1):
    print((' '*x)+'*'*z+(' '*x))
    x -= 1
    z += 2
print('')
pust = 2*n-1
x = n-1
z = 1
for i in range(1, n+1):
    print((' ' * x) + '*' * z+(' ' * pust) + '*'*z+(' '*x))
    x -= 1
    z += 2
    pust -= 2