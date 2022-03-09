''' Fa un fisier ex4 in care faci o functie care primeste 2 param (unul pe care il cautam si o lista). 
functia sa intoarca true sau false. incearca sa o faci in mai multe moduri '''


def searchElem(x, lista):
    for a in lista:
        print(a)
        if x == a:
            return True
    return False

# listuta = [27, "Superman", 41.1, 12j, "Marius", "Eu"]
# y = "Titi"

# rezultat = searchElem(y, listuta)
# print(rezultat)

# def DemoIterativ(x):
#     while x < 10:
#         print(x)
#         x = x + 1

#     return 10

# def DemoRecursiv(x):
#     if x < 10:
#         print(x)
#         x = x + 1
#         return DemoRecursiv(x)
#     else:
#         return 10
    
# DemoIterativ(2)
# print("---")
# DemoRecursiv(2)

# sir = [1, 3, 6, 7, 12, 13, 54, 77, 78]
# z = 54

# 
def searchBinar(x, lista):
    mijlocLista = int(len (lista) / 2)
    print(mijlocLista)
    if x == lista[mijlocLista]:
        return True     #cazul de baza
    elif len(lista) == 1:
        return False
    elif x < lista[mijlocLista]:
        return searchBinar(x, lista[:mijlocLista])
    elif x > lista[mijlocLista]:
        return searchBinar(x, lista[mijlocLista:])

# sir_simplu = [10, 20, 35, 50]
# x_simplu = 240

# rezultat_searchBinar = searchBinar(x_simplu, sir_simplu)
# print(rezultat_searchBinar)

sir_mare = []
for i in range(10000000):
    sir_mare.append(i)

# print(searchBinar(5000976, sir_mare))
print(searchElem(5000976, sir_mare))