
def area(a, b, c):
    pass # непонял зачем
    s=(a+b+c)/2
    triangle_area = (s*(s-a)*(s-b)*(s-c))**(0.5)
    return triangle_area
a = 6
b = 7
c = 9

triangle_area = area(a, b, c)
print("площадь равна:", triangle_area)