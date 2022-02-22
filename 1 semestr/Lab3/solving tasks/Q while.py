# Q
F0 = 0
F1 = 1
A = int(input())
summa = 0
x = 1
flag = 0

while x > -1:
    if A == summa:
        flag = 1
        schet = x
    if A <= summa:
        break
    summa = F0 + F1
    F0 = F1
    F1 = summa

    x += 1
if A == 0 or A == 1:
    print(x-1)
elif flag == 1:
    print(schet)
else:
    print(-1)