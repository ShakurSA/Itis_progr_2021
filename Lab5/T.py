# T
x = str(input())
p = ''
for i in range (0, len(x)):
    if i % 3 != 0:
        p = p + x[i]
print(p)