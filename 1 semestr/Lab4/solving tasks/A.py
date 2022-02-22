# A
n = int(input())
x = 1
summnechet = 0
proizchet = 1
sumotric = 0
proizpolozh = 1
while x <= n:
    n1 = int(input())
    if n1 % 2 == 0:
        proizchet *= n1
    if n1 % 2 != 0:
        summnechet += n1
    if n1 < 0:
        sumotric += n1
    if n1 > 0:
        proizpolozh *= n1
    x += 1
if proizchet == 1:
    print('Net chet')
elif proizchet != 1:
    print('Proizv chet:', proizchet)
if proizpolozh == 1:
    print('Net polozh')
elif proizpolozh != 1:
    print('Proizv polozh:', proizpolozh)
if summnechet == 0:
    print('Net nechet')
elif summnechet != 0:
    print('Summa nechet:', summnechet)
if sumotric == 0:
    print('Net otric')
elif sumotric != 0 :
    print('Summa otric:', sumotric)