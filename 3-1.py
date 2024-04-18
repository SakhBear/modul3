
x = float(input('первый взнос:'))
y = float(input("желаемая сумма:"))
p = float(input("процентная ставка:"))
g = 0
while x < y:
    x= x * (1+p/100)
    x=int(100 * x) / 100
    g+= 1
print("необходимое количество лет", g)
