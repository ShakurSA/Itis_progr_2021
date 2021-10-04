# H
n = int(input())
x = 1
count = 0
flag = 0
while x <= n:
    z = int(input())
    if z == 0:
        flag = 1
    elif flag == 0:
        count += 1
    x += 1
print(count)