# T
kon = 0
n = int(input())
x = 1
count = 0
while x < n:
    b = x
    kon = 0
    while b > 0:
        kon = kon * 10
        kon = kon + b % 10
        b = b // 10
    if x == kon:
        count += 1
    x += 1
print(count)
