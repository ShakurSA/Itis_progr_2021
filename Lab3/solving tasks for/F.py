# F
n = int(input())
m = 0
for x in range(1, n+1, 1):
    s = int(input())
    if s == 0:
        m += 1
print(m)