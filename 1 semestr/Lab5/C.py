# C
import math
P = int(input())
X = int(input())
Y = int(input())
K = int(input())
S = 100 * X + Y

for i in range(K):
    S += int(S * P / 100)
    S = math.floor(S)
print(S // 100, S % 100)