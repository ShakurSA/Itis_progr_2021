# M
n = int(input())
z = n
flag = 0
for i in range(2, n//2):
    while z % i == 0 and z > 0:
        z = z / i
        flag += 1
        print(i)
if flag == 0:
    print('Net deliteley')