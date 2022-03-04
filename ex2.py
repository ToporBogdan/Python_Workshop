# creeaza 2 functii. fiecare primeste un parametru de tip lista. functiile vor intoarce min/max din lista respectiva.
from ex1 import switch 
listuta = [1, 3, 5, 1, 654, 121, 0]

def functieMin(lista): 
    param = 999999
    for x in lista:
        if x < param:
            param = x
    return param 

def functieMax(lista):
    param = 0
    for x in lista:
        if x > param:
            param = x
    return param 

minlistuta = functieMin(listuta)
print("Minimul din lista este: " + str(minlistuta))
maxlistuta = functieMax(listuta)
print("Maximul din lista este: " + str(maxlistuta))

# print(min(listuta))
# print(max(listuta))

# provizoriu = minlistuta 
# minlistuta = maxlistuta
# maxlistuta = provizoriu 

# print(minlistuta, maxlistuta)

switch(minlistuta, maxlistuta)







