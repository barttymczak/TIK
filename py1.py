import math

print("kuflowe najlepsze")

def suma(lista):
    x=0
    for i in range(len(lista)):
       x=lista[i] + x
    return x

def equation(a, b, c):

    wyr=(b**2 - (4*a*c))
    if wyr<0:
        return math.nan()
    else:
        x1=((-b-math.sqrt(wyr))/(2*a))
        x2=((-b+math.sqrt(wyr))/(2*a))
    return wyr, x1, x2

a=1
b=4
c=4

print(equation(a,b,c))
lista=[1,2,3,4,5,6]
print(lista)
lista.append(7)
print(lista, len(lista), lista[-3], lista[len(lista)-2])
print(lista[3:6])

for element in lista:
    print(element, math.cos(element))
for i in range(len(lista)):
    print(lista[i], math.cos(lista[i]))

print(suma(lista))
