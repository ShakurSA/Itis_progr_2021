# L
n = int(input())
maxi = 0
while n != 0:
    if n > maxi:
        maxi = n
    n = int(input())
print(maxi)