#insertar elementos en una lista y mostrara el estado de la estructura en orden
lista = []
tamaño = int(input("Cuantos elementos quieres en la lista"))


def Insertar(t, lst):
    cont=0
    while (cont<t):
        elem=object(input("Dame el elemento a insertar"))
        list.append(elem)
        cont+=1
def Mostrar(lista):
    print(lista)
    
def burbuja(lst):
    for i in range(0, len(lst)-1):
        for j in range(0,len(lst)-i-1):
            if(lst[j]>lst[j+1]):
                lst[j],lst[j+1] = lst[j+1],lst[j]
    
Insertar(tamaño, lista)
Mostrar(lista)
burbuja(lista)
Mostrar(lista)