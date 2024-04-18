
from random import randint
n = 5
m = [[randint(0,100) for i in range(n)] for j in range (n)]
big_n=0
for i in m:
    for j in i:
        if j > big_n:
            big_n=j
print (*m, sep='\n')
print("наибольшее число",  big_n)