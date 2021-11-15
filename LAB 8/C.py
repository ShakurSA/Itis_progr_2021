n = int(input())
def c(n):
    for i in range(7):
        s = int((pow(n, (1/3))))
        n = n - s ** 3
        if s != 0:
            print(s, end=' ')

c(n)