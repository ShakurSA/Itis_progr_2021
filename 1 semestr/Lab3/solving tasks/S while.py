# S
kon = 0
n = int(input())
while n > 0:
    kon = kon * 10
    kon = kon + n % 10
    n = n // 10

print (kon)