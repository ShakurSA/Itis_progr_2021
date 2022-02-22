# O
a = int(input())
b = int(input())
c = int(input())
maxi = 0
med = 0
mini = 0
if a >= b and a >= c:
    maxi = a
elif b >= c:
    maxi = b
else:
    maxi = c
if maxi-a >= maxi-b and maxi-a >= maxi-c:
    mini = a
elif maxi-b >= maxi-c and maxi-b >= maxi-c:
    mini = b
else:
    mini = c
if maxi != a and mini != a:
    med = a
if maxi != b and mini != b:
    med = b
if maxi != c and mini != c:
    med = c
if mini+med > maxi:
    if maxi**2 == med**2+mini**2:
        print('rectangular')
    if maxi**2 < med**2+mini**2:
        print('acute')
    if maxi**2 > med**2+mini**2:
        print('obtuse')
else:
    print('impossible')