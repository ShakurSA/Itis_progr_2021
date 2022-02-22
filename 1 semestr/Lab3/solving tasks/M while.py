# M
n = int(input())
count = 0
proshl = 0
while n != 0:
    proshl = n
    n = int(input())
    if n > proshl:
        count += 1
print(count)