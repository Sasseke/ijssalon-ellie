import math

print("Voor de formule ax^2 + bx + c, geef a, b en c:")
a = int(input("Wat is a?"))
b = int(input("Wat is b?"))
c = int(input("Wat is c?"))

def discriminant(a,b,c):
    try:
       D1 = (-b + math.sqrt(b**2 - 4*a*c))/(2 * a)
       D2 = (-b - math.sqrt(b**2 - 4*a*c))/(2 * a)
    except:
       D1 = "geen oplossing"
       D2 = "geen oplossing"
    
    uitvoer = [D1,D2]
    return uitvoer

uitkomst = discriminant(a,b,c)
D1 = uitkomst[0]
D2 = uitkomst[1]

print(f"De waarde van a is {a}, de waarde van b is {b}, de waarde van c is {c}. De uitkomst van D1 is {D1} en de uitkomst van D2 is {D2}")