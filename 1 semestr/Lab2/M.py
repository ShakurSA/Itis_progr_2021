# M
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
print(mini, med, maxi)