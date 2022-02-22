a = int(input())
b = int(input())
def F(a,b):
    if a == b:
        print(a)
    else:
        while a != 0 and b != 0:
            if a > b and b != 0:
                a = a % b
            if a < b and a != 0:
                b = b % a
        print(a+b)
F(a,b)