# P
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
if (A <= D and B <= E) or (A <= E and B <= D):
    print('YES')
elif (A <= D and C <= E) or (C <= E and A <= D):
    print('YES')
elif (B <= D and C <= E) or (C <= E and B <= D):
    print('YES')
else:
    print('NO')