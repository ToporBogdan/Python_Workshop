'''
am o lista de elem (nr zecimale), gaseste totalitatea / toate tuplurile care pot fi lungimi de laturi pt un triunghi. 
'''
from pprint import pprint 

lista = [11, 41, 5, 17, 2, 35, 16]

def FindTriangles(num):
    tupluriTriunghiuri = []
    for i in range(len(num)):
        for j in range(len(num)):
            for k in range(len(num)):
                lat1 = num[i]
                lat2 = num[j]
                lat3 = num[k]
                if lat1 + lat2 > lat3 and lat2 + lat3 > lat1 and lat3 + lat1 > lat2:
                    triunghi = (lat1, lat2, lat3)
                    # print(triunghi)
                    tupluriTriunghiuri.append(triunghi)
    return tupluriTriunghiuri

print(FindTriangles(lista))
# pprint(FindTriangles(lista))




