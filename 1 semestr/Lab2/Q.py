# Q
a1 = int(input())
b1 = int(input())
c1 = int(input())
maxi1 = 0
med1 = 0
mini1 = 0
if a1 >= b1 and a1 >= c1:
    maxi1 = a1
elif b1 >= c1:
    maxi1 = b1
else:
    maxi1 = c1
if maxi1-a1 >= maxi1-b1 and maxi1-a1 >= maxi1-c1:
    mini1 = a1
elif maxi1-b1 >= maxi1-c1 and maxi1-b1 >= maxi1-c1:
    mini1 = b1
else:
    mini1 = c1
if maxi1 != a1 and mini1 != a1:
    med1 = a1
if maxi1 != b1 and mini1 != b1:
    med1 = b1
if maxi1 != c1 and mini1 != c1:
    med1 = c1
a2 = int(input())
b2 = int(input())
c2 = int(input())
maxi2 = 0
med2 = 0
mini2 = 0
if a2 >= b2 and a2 >= c2:
    maxi2 = a2
elif b2 >= c2:
    maxi2 = b2
else:
    maxi2 = c2
if maxi2-a2 >= maxi2-b2 and maxi2-a2 >= maxi2-c2:
    mini2 = a2
elif maxi2-b2 >= maxi2-c2 and maxi2-b2 >= maxi2-c2:
    mini2 = b2
else:
    mini2 = c2
if maxi2 != a2 and mini2 != a2:
    med2 = a2
if maxi2 != b2 and mini2 != b2:
    med2 = b2
if maxi2 != c2 and mini2 != c2:
    med2 = c2
if maxi1 == maxi2 and med1 == med2 and mini1 == mini2:
    print("Boxes are equal")
elif maxi1 >= maxi2 and med1 >= med2 and mini1 >= mini2:
    print("The first box is larger than the second one")
elif maxi2 > maxi1 and med2 > med1 and mini2 > mini1:
    print("The first box is smaller than the second one")
else:
    print("Boxes are incomparable")
