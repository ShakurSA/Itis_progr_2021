# P
x = str(input())
a = (x[x.find('h')+1:]) + (x[:x.rfind('h')])
a = a.replace('h', 'H')
print(x[:x.find('h')+1] + a + x[x.rfind('h'):])