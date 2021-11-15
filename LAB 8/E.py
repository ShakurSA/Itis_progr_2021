n = int(input())
m = int(input())
p = n
q = m
def E(n, m):
    while n != m:
        if n > m:
            n = n - m
        else:
            m = m - n
    print(p//n, q//m)
E(n,m)