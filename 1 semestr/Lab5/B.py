# B
P = int(input('percents'))
x = int(input('rubles'))
y = int(input('penny'))
summa = 0
P = 1 + P / 100
x = x * 100 + y
summa = x * P
summa = round(summa)
print(int(summa // 100), int(summa % 100))