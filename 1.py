# fa o functie care primeste 2 parametri a si b si le schimba valorile intre ele si le printeaza la ecran. 
from calendar import c
from re import X


xglobal = 2
yglobal = 1021

def switch(a, b):
    c = a
    a = b
    b = c
    print("a:" + str(a), "b:" + str(b))    

# switch(10, 15)
switch(xglobal, yglobal) 
print("a:" + str(xglobal), "b:" + str(yglobal))    









