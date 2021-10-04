# K
n = int(input())
count = 0
while n != 0:
    if n % 2 == 0:
        count += 1
    n = int(input())
print(count)