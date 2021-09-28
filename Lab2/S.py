# S
n = int(input())
if (n % 10 > 4) or (n % 10 == 0):
    print(n, 'korov')
elif n % 10 == 1:
    print(n, 'korova')
else:
    print(n, 'korovi')