# K
A = int(input())
B = int(input())
for x in range(A, B+1, 1):
    c = x // 100
    d = x % 100
    if x // 1000 == x % 10 and c % 10 == d // 10:
        print(x)