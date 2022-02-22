# N
for i in range(1, 5000+1, 1):
    summa = 0
    delit = 2
    while delit < (i**0.5):
        if i % delit == 0:
            summa += delit
            summa += (i / delit)
        delit += 1
    if (summa+1) == i and summa != 0:
        print(i)