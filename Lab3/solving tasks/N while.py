# N
maxi = 0
n = int(input())
polumaxi = 0
while n != 0:
    if n >= maxi:   
        polumaxi = maxi 
        maxi = n
    if n > polumaxi and n < maxi:
    	polumaxi = n
    n = int(input())
print(polumaxi)