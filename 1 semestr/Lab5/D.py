# D
import math
x = float(input())
x = x * 100
a = math.floor(x // 100)
b = math.floor(x % 100)
print(int(a),int(b))