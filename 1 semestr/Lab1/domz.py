# A
N = int(input('kol-vo shkol'))
K = int(input('kol-vo yablok'))
print(K // N)

# B
N = int(input('kol-vo shkol'))
K = int(input('kol-vo yablok'))
print(K % N)

# C
N = int(input("2^"))
print(2 ** N)

# D
N = int(input())
print(N % 10)


# E
N = int(input())
print(N // 10)

# F
N = int(input())
print((N//10) % 10)

# H
N = input()
F = input()
N, F = F, N
print(N, F)

# I
N = int(input())
if N % 2 == 0:
    N += 2
else:
    N += 1
print(N)

# J
A = 'A'
print(A*100)

# K
N = int(input())
N1 = '    _~_    '
N2 = '   (o o)   '
N3 = '  /  V  \  '
N4 = ' /(  _  )\ '
N5 = '   ^^ ^^   '
 
print(N1*N)
print(N2*N)
print(N3*N)
print(N4*N)
print(N5*N)

# L
N = int(input())
print(str(N)*100)
N = int(N)**2
print(str(N))

# M
N = str(input('name'))
C = '!'
N = N+C
print('Hello,', N)

# N
N = int(input())
M = N+1
L = N-1
print('number for the number', N, 'is', (str(M)+'.'))
print('ious number for the number', N, 'is', (str(L)+'.'))

# O
v = int(input('speed'))
t = int(input('time'))
if v*t >= 109:
    print((v*t) % 109)
else:
    print(v*t)

# P
N = int(input())
print(N//60, N % 60)

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

#R
A = float(input('rub'))
B = float(input('kop'))
N = float(input('pir'))
N = (A*100+B)*N
A = N//100
B = N % 100
print(int(A), int(B))

# S
H1 = float(input('HOURS1'))
M1 = float(input('minutes1'))
S1 = float(input('sec1'))
H2 = float(input('h2'))
M2 = float(input('m2'))
S2 = float(input('s2'))
print(int((H2*3600+M2*60+S2)-(H1*3600+M1*60+S1)))

# T
N = float(input('v'))
M = float(input('s'))
if M % N != 0:
    print(int(M//N+1))
else:
    print(int(M//N))

# U
H = int(input('shest'))
A = int(input('vverh'))
B = int(input('vniz'))
if H % (A-B) != 0:
    print(H//(A-B)+1)
else:
    print(H//(A-B))

# V
N = int(input())
if N//1000 != 0:
    A = N//100
    A = A % 10
    B = N % 100
    B = B//10
    if A == B and (N//1000 == N % 10):
        print('1')
    else:
        print('0')
if N % 10 == 0 and N//1000 == 0 and N//100 != 0:
    A = N//10
    A = A % 10
    if A == N//100:
        print('1')
    else:
        print('0')
if N//100 == 0:
    print('0')

# W
A = int(input())
B = int(input())
D = A - B
D = D ** 2
D = D ** 0.5
print((A+B+D) / 2)

# X
A = int(input())
B = int(input())
C = A % B
print(bool(not C))
	