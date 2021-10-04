# U
n = int(input())
maxi = 0
count = 1
while n != 0:
    n1 = n
    n = int(input())
    if n == n1:
        count += 1
    if count > maxi:
        maxi = count
    if n != n1:
        count = 1
print(maxi)