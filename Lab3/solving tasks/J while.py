# J
n = int(input())
count = 0
summa = 0
while n != 0:
    count += 1
    summa += n
    n = int(input())
print(float(summa/count))