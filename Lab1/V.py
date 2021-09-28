# V
N = int(input())
if N//1000 != 0:
    A = N//100
    A = A % 10
    B = N % 100
    B = B//10
    if A == B and (N//1000 == N % 10):
        print('1')
    else:
        print('0')
if N % 10 == 0 and N//1000 == 0 and N//100 != 0:
    A = N//10
    A = A % 10
    if A == N//100:
        print('1')
    else:
        print('0')
if N//100 == 0:
    print('0')