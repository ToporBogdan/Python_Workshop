from ex1 import switch 

def sortare(lista):
    initial = lista[0]    
    for i in range(1, len(lista)):
        if lista[i] < initial:
            switch(initial, lista[i])
            # print(lista[i])
lista = [26, 12, 111, 143, 665, 2, 11, 4]

sortare(lista)
print(lista)