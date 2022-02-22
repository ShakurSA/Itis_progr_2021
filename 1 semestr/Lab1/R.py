#R
A = float(input('rub'))
B = float(input('kop'))
N = float(input('pir'))
N = (A*100+B)*N
A = N//100
B = N % 100
print(int(A), int(B))