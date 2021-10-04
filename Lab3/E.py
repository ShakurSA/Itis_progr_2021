# E
n = int(input())
for x in range(n):
    print("+___", end=" ")
print()
for x in range(1, n+1):
    print('|'+str(x),"/ ", end="")
print()
for x in range(n):
    print("|__\\", end=" ")
print()
for x in range(n):
    print("|   ", end=" ")
print()