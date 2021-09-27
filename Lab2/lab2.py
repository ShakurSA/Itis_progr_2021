# #A
# A = int(input())
# B = int(input())
# if A >= B:
#     print(A)
# else:
#     print(B)

# # B
# A = int(input())
# B = int(input())
# if A > B:
#     print(1)
# if A < B:
#     print(2)
# if A == B:
#     print(0)

# #C
# A = int(input())
# if A > 0:
#     print(1)
# if A < 0:
#     print(-1)
# if A == 0:
#     print(0)

# #D
# A = int(input())
# B = int(input())
# C = int(input())
# if A >= B and A >= C:
#     print(A)
# elif B >= C:
#     print(B)
# else:
#     print(C)

# # E
# a1, b1 = int(input()), int(input())
# a2, b2 = int(input()), int(input())
# if (a1*a2) > 0 and (b1*b2) > 0:
#     print('YES')
# else:
#     print('NO')

# # F
# A = int(input())
# if ((A%4==0) and (A%100!=0)) or (A%400==0):
#     print('YES')
# else:
#     print('NO')

# # G
# a1, b1 = int(input()), int(input())
# a2, b2 = int(input()), int(input())
# c = a1-a2
# d = b1-b2
# if ((c > 1) or (c < -1)) or ((d > 1) or (d < -1)):
#     print('NO')
# else:
#     print('YES')

# # H
# A = int(input())
# B = int(input())
# C = int(input())
# if (A % 2 == 0 or B % 2 == 0 or C % 2 == 0) and (A % 2 == 1 or B % 2 == 1 or C % 2 == 1):
#     print('YES')
# else:
#     print ('NO')

# # I
# a = int(input())
# b = int(input())
# c = b - a + 1
# if (a - 1) % c == b % c == 0:
#     print('YES')
# else:
#     print('NO')

# # J
# a1, b1 = int(input()), int(input())
# a2, b2 = int(input()), int(input())
# c = a1 - a2
# d = b1 - b2
# if (c == d) or (c % 2 == 0 and d % 2 == 0) or (c % 2 == 1 and d % 2 == 1):
#     print('YES')
# else:
#     print('NO')

# # K
# n = int(input())
# m = int(input())
# k = int(input())
# if (k % n == 0) or (k % m == 0):
#     print('YES')
# else:
#     print('NO')

# L
# a1, b1 = int(input()), int(input())
# a2, b2 = int(input()), int(input())
# c = b1+(a2-a1)
# d = b1-(a2-a1)
# if (a2-a1 > 0) and (b2 < c) and (b2 > d) and (a2+b2 % 2 != 0):
#     print('YES')
# else:
#     print('NO')

# # M
# a = int(input())
# b = int(input())
# c = int(input())
# maxi = 0
# med = 0
# mini = 0
# if a >= b and a >= c:
#     maxi = a
# elif b >= c:
#     maxi = b
# else:
#     maxi = c
# if maxi-a >= maxi-b and maxi-a >= maxi-c:
#     mini = a
# elif maxi-b >= maxi-c and maxi-b >= maxi-c:
#     mini = b
# else:
#     mini = c
# if maxi != a and mini != a:
#     med = a
# if maxi != b and mini != b:
#     med = b
# if maxi != c and mini != c:
#     med = c
# print(mini, med, maxi)

# # N
# a = int(input())
# b = int(input())
# c = int(input())
# x = 0
# if a == b:
#     x += 1
# if a == c:
#     x += 1
# if b == c:
#     x += 1
# if x == 1:
#     x += 1
# print(x)

# # O
# a = int(input())
# b = int(input())
# c = int(input())
# maxi = 0
# med = 0
# mini = 0
# if a >= b and a >= c:
#     maxi = a
# elif b >= c:
#     maxi = b
# else:
#     maxi = c
# if maxi-a >= maxi-b and maxi-a >= maxi-c:
#     mini = a
# elif maxi-b >= maxi-c and maxi-b >= maxi-c:
#     mini = b
# else:
#     mini = c
# if maxi != a and mini != a:
#     med = a
# if maxi != b and mini != b:
#     med = b
# if maxi != c and mini != c:
#     med = c
# if mini+med > maxi:
#     if maxi**2 == med**2+mini**2:
#         print('rectangular')
#     if maxi**2 < med**2+mini**2:
#         print('acute')
#     if maxi**2 > med**2+mini**2:
#         print('obtuse')
# else:
#     print('impossible')

# # P
# A = int(input())
# B = int(input())
# C = int(input())
# D = int(input())
# E = int(input())
# if (A <= D and B <= E) or (A <= E and B <= D):
#     print('YES')
# elif (A <= D and C <= E) or (C <= E and A <= D):
#     print('YES')
# elif (B <= D and C <= E) or (C <= E and B <= D):
#     print('YES')
# else:
#     print('NO')

# # Q
# a1 = int(input())
# b1 = int(input())
# c1 = int(input())
# maxi1 = 0
# med1 = 0
# mini1 = 0
# if a1 >= b1 and a1 >= c1:
#     maxi1 = a1
# elif b1 >= c1:
#     maxi1 = b1
# else:
#     maxi1 = c1
# if maxi1-a1 >= maxi1-b1 and maxi1-a1 >= maxi1-c1:
#     mini1 = a1
# elif maxi1-b1 >= maxi1-c1 and maxi1-b1 >= maxi1-c1:
#     mini1 = b1
# else:
#     mini1 = c1
# if maxi1 != a1 and mini1 != a1:
#     med1 = a1
# if maxi1 != b1 and mini1 != b1:
#     med1 = b1
# if maxi1 != c1 and mini1 != c1:
#     med1 = c1
# a2 = int(input())
# b2 = int(input())
# c2 = int(input())
# maxi2 = 0
# med2 = 0
# mini2 = 0
# if a2 >= b2 and a2 >= c2:
#     maxi2 = a2
# elif b2 >= c2:
#     maxi2 = b2
# else:
#     maxi2 = c2
# if maxi2-a2 >= maxi2-b2 and maxi2-a2 >= maxi2-c2:
#     mini2 = a2
# elif maxi2-b2 >= maxi2-c2 and maxi2-b2 >= maxi2-c2:
#     mini2 = b2
# else:
#     mini2 = c2
# if maxi2 != a2 and mini2 != a2:
#     med2 = a2
# if maxi2 != b2 and mini2 != b2:
#     med2 = b2
# if maxi2 != c2 and mini2 != c2:
#     med2 = c2
# if maxi1 == maxi2 and med1 == med2 and mini1 == mini2:
#     print("Boxes are equal")
# elif maxi1 >= maxi2 and med1 >= med2 and mini1 >= mini2:
#     print("The first box is larger than the second one")
# elif maxi2 > maxi1 and med2 > med1 and mini2 > mini1:
#     print("The first box is smaller than the second one")
# else:
#     print("Boxes are incomparable")


# # R
# a1 = int(input())
# b1 = int(input())
# c1 = int(input())
# maxi1 = 0
# med1 = 0
# mini1 = 0
# if a1 >= b1 and a1 >= c1:
#     maxi1 = a1
# elif b1 >= c1:
#     maxi1 = b1
# else:
#     maxi1 = c1
# if maxi1-a1 >= maxi1-b1 and maxi1-a1 >= maxi1-c1:
#     mini1 = a1
# elif maxi1-b1 >= maxi1-c1 and maxi1-b1 >= maxi1-c1:
#     mini1 = b1
# else:
#     mini1 = c1
# if maxi1 != a1 and mini1 != a1:
#     med1 = a1
# if maxi1 != b1 and mini1 != b1:
#     med1 = b1
# if maxi1 != c1 and mini1 != c1:
#     med1 = c1
# a2 = int(input())
# b2 = int(input())
# c2 = int(input())
# maxi2 = 0
# med2 = 0
# mini2 = 0
# if a2 >= b2 and a2 >= c2:
#     maxi2 = a2
# elif b2 >= c2:
#     maxi2 = b2
# else:
#     maxi2 = c2
# if maxi2-a2 >= maxi2-b2 and maxi2-a2 >= maxi2-c2:
#     mini2 = a2
# elif maxi2-b2 >= maxi2-c2 and maxi2-b2 >= maxi2-c2:
#     mini2 = b2
# else:
#     mini2 = c2
# if maxi2 != a2 and mini2 != a2:
#     med2 = a2
# if maxi2 != b2 and mini2 != b2:
#     med2 = b2
# if maxi2 != c2 and mini2 != c2:
#     med2 = c2
# n = (maxi1 // maxi2) * (med1 // med2) * (mini1 // mini2)
# print(n)

# # S
# n = int(input())
# if (n % 10 > 4) or (n % 10 == 0):
#     print(n, 'korov')
# elif n % 10 == 1:
#     print(n, 'korova')
# else:
#     print(n, 'korovi')

# # T
# k = int(input())
# if (k % 3 == 0) or (k % 5 == 0):
#     print('YES')
# else:
#     print('NO')

# U
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == 0 and b == 0:
    print('INF')
elif a == 0 or b*c == a*d:
    print('NO')
elif b % a == 0:
    x = -b // a
    print(x)
else:
    print('NO')
