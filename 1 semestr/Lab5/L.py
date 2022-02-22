# L
x = str(input())
count = 0
for i in range(1, len(x)):
    if x[i] == ' ':
        count += 1
print(count)