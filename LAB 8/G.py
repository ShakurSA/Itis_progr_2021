a = int(input())
n = int(input())
def G(a,n):
    if n % 2 == 0:
        a = a ** ((2)*(n//2))
    else:
        a = a * a ** (n-1)
    print(a)
G(a,n)