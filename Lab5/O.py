# O
x = str(input())
a = x.find('f')
b = x.rfind('f')
if a == b:
    print(a)
if a < b:
    print(a, b)