# Escribe una función llamada recortar que toma una lista y la modifica, removiendo el primer y último
# elemento. Después escribe una función llamada medio que toma una lista y regresa una nueva lista que contiene
# todo excepto el elemento o elementos medios.
import math
lista = []
tamaño = int(input("Cuantos elementos quieres en la lista"))


def Insertar(t, lst):
    cont = 0
    while(cont < t):
        elem = input("Dame el elemento a insertar")
        lst.append(elem)
        cont += 1


def Mostrar(lst):
    print(lst)


def Recortar(lst):
    lst.pop(0)
    lst.pop()


def Medios(lst):
    # Cuando el tamaño de la lista es par se toman lo elementos medio (2)
    l = len(lst)
    if (l % 2 == 0):
        sup = int(l / 2)  # se cpnvierte a entero para sacar su parte entera
        inf = sup-1
        del lst[inf:sup+1]
    else:
        sup = math.floor(l/2)
        del lst[sup]
    listaN = lst
    return listaN


Insertar(tamaño, lista)
Mostrar(lista)
Recortar(lista)
Mostrar(lista)
Mostrar(Medios(lista))
