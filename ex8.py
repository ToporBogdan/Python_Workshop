'''
Să se afișeze toate permutările circulare a cifrelor unui număr.

Exemplu:
Pentru numărul 12345 se va afișa:
51234
45123
34512
23451
12345

Hint: Gândește-te cum rezolvi problema pentru un string, apoi extinzi la cifre ale unui număr.

b) fa ex si recursiv
'''

numar = 123456789

def Permutari(numar):
    numar = str(numar)
    CarSeparat = list(numar.strip())
    for i in range(len(numar)):
        aux1 = CarSeparat.pop()
        CarSeparat.insert(0, aux1)
        numar = CarSeparat
        print(int("".join(numar)))

print("Să se afișeze toate permutările circulare a cifrelor numărului:" + str(numar))
Permutari(numar)