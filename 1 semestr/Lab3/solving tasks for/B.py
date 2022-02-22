# B
A = int(input())
B = int(input())
if A <= B:
    print(range(A, B+1, 1))
if A > B:
    print(range(A, B-1, -1))