
def H(a,n):
    s = a
    for i in range(n):
        a *= s
    return a
print(H(int(raw_input()), int(raw_input())))