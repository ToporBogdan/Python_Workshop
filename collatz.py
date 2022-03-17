"""
primesti un nr, faci collatz conjecture(daca impar = x3+1; daca par = /2). 
ajungem la 1 si ne oprim. afiseaza nr de pasi facuti pana ajungi la 1. (recursiv)
"""

def collatz(numar):
    numar = int(InputTastatura)
    pasi = 0
    while numar != 1:
        if numar % 2 == 1:
            numar = 3 * numar + 1
            pasi += 1
        if numar % 2 == 0:
            numar = numar / 2
            pasi += 1
    return pasi

while True:
    try:
        InputTastatura = input("Introduceti un numar: ")
        print("Numarul de pasi dupa Collatz Conjuncture:", collatz(InputTastatura))
        break
    except ValueError:
        print("Va rugam sa introduceti un numar intreg")

"""
CIORNA
"""

# InputTastatura = input("Introduceti un numar: ")
# x = InputTastatura
# print(type(x))
# y = float(InputTastatura)
# print(type(y))

# var = input("Hi! I like cheese! Do you like cheese?").lower()
# if var == "yes":
#   print("That's awesome!")