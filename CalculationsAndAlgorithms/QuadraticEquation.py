import math

a=int(input("Wprowadz a: "))
b=int(input("Wprowadz b: "))
c=int(input("Wprowadz c: "))

d=b*b-(4*a*c)

if(d==0):
    x1 = -b/(2*a)
    print("Wartosc pierwiastka: " + str(x1))
elif(d>0):
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("Wartosc pierwiastkow: " + str(x1) + " " + str(x2))
else:
    x1 = None
    x2 = None
    print("Brak pierwiastkow")