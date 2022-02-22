# I
x = str(input())
count = 0
for i in range (0, len(x)):
    if x[i] == 'f':
        count += 1
        if count == 2:
            print(i)
if count == 1:
    print(-1)
if count == 0:
    print(-2)