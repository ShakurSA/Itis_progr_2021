# D
n = int(input())
x = float(input())
past = 1
s = 0
for i in range(1, n+1, 1):
    s += (x+i) * past
    past *= (x+i)
print(s)