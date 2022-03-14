"""
Se da un text citit de la tastatura, care poate contine orice dar si cifre. 
Sa spun de cate ori apare fiecare cifra. (sau fiecare caracter in parte, de cate ori apare)

SN: vector de referinta / frequency array / counter array
"""
from cmath import e
from pprint import pprint
from string import ascii_lowercase
from tokenize import Name
from unittest import expectedFailure
from xml.dom import NamespaceErr

InputTastatura = input("Enter a text here: ")
# print(type(InputTastatura))
# CharCautat = input("Type the character you want to count: ")

# def FindChar(InputTastatura, CharCautat):
#     aux = 0
#     for CurrentChar in InputTastatura:
#         if CurrentChar == CharCautat:
#             aux = aux + 1
#     return aux

# print(FindChar(InputTastatura, CharCautat))

# def FindCharJmen(InputTastatura):
#     L = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     for CurrentChar in InputTastatura:
#         if CurrentChar >= "0" and CurrentChar <= "9":
#             L[int(CurrentChar)] += 1
#     return L
# print(FindCharJmen(InputTastatura)) 

S = {}
for i in range(0, 10):
        i = str(i)
        S[i] = 0
for c in ascii_lowercase:
        S[c] = 0
    # print(S)
def FindCharMaiJmen(InputTastatura):
    for CurrentChar in InputTastatura:
        try:  
            S[CurrentChar] += 1
        except KeyError:
            print('Pula')
        except NameError:
            print('Pizda')
    return S
pprint(FindCharMaiJmen(InputTastatura))







