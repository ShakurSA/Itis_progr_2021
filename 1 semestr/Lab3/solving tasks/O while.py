# O
n = int(input())
count = 0
maxi = 0
while n != 0:
    if n > maxi:
        maxi = n
        count = 0
    if n == maxi:
        count += 1
    n = int(input())
print(count)