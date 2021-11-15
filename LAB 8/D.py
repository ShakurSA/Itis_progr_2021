def D():
    n = int(input())
    if n != 0:
        D()
        if (n**0.5) == int(n**0.5):
            global s
            s = 0
            print(n, end=' ')
s = 1
D()
if s:
    print(0)