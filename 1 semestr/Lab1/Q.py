# Q
N = int(input())
H = N//3600
N = N % 3600
M = N//60
if M < 10:
    M = ('0'+str(M))
S = N % 60
if S < 10:
    S = ('0'+str(S))
print(str(H)+':'+str(M)+':'+str(S))