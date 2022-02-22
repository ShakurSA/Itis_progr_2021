# T
N = float(input('v'))
M = float(input('s'))
if M % N != 0:
    print(int(M//N+1))
else:
    print(int(M//N))