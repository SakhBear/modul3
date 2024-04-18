
l = [1, 4, 1, 6, "hello", "a", 5, "hello"]
l2 =[]
l3 =[]
for i in l:
    if not i in l2:
        l2.append(i)
    else:
         l3.append(i)
print(l)
print(l2)
print(l3)