# O
v = int(input('speed'))
t = int(input('time'))
if v*t >= 109:
    print((v*t) % 109)
else:
    print(v*t)