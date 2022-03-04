# scrieti o functie care primind un nr natural, intoarce o valoare True sau False insemnand ca nr este palindrom sau nu.
def palindromLiceu(x):
    listaCifre = []
    while x != 0:
        listaCifre.append(x % 10)
        x = int(x / 10)
    return palHelp(listaCifre)

def palindromString(x):
    xString = str(x)
    for z in xString:
        z = int(z)
    return palHelp(xString)

def palHelp(r):
    for y in range(0, int(len(r) / 2)):
        if r[y] != r[len(r) - y - 1]:
            return False
    return True

print(palindromLiceu(1234321)) 
print(palindromString(1234321)) 
