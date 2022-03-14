'''
Facem o functie pt Bubble Sorting
'''
# from ex1 import switch
# def switch(a, b):
    # print("a:" + str(a), "b:" + str(b))
    # c = a
    # a = b
    # b = c
    # print("a:" + str(a), "b:" + str(b))


# def SwitchElementsInList(myList, firstIndex, secondIndex):
#     # print(myList)
#     aux = myList[firstIndex]
#     myList[firstIndex] = myList[secondIndex]
#     myList[secondIndex] = aux
#     # print(myList)
#     return myList    

# lista = [5, 2, 16, 11, 9, 4]
# def BubbleSort(num):
#     for j in range(len(num)):
#         for i in range(j+1, len(num)):
#             print(j, i)
#             if num[j] > num[i]: 
#                 num = SwitchElementsInList(num, j, i)
#     return num
    
# print(BubbleSort(lista))


def GetMin(list):
    min = list[0]
    for i in range(len(list)):
        if list[i] < min:
            min = list[i]
    return min

lista = [5, 2, 16, 11, 9, 4]

def MinSort(myList):
    listaAux = []
    for i in range(len(myList)):
        min = GetMin(myList)
        listaAux.append(min)
        myList.remove(min)

    return myList, listaAux
print(MinSort(lista))



