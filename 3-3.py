
n = int(input('введите число :'))
sum = 0
while n!= 0:
    p = n%10
    sum +=p
    n = n // 10

print(sum)