#programa que almace los números que el usuario ingrese en una lista, terminar la inserción cuando el usuario 
# ingrese “fin”, y utiliza las funciones max() y min() para calcular el máximo y el mínimo después
#de que el bucle termine.

import math
lista = []

def Insertar (lst):
    i=0
    while (i != 'fin' ):
        elem=int(input ("Ingresa el elemento "))
        lst.append(elem)
        i=elem
    lst.pop()
    
def Mostrar (lst):
    print (lst)
    print("el valor maximo es: ", max(lista))
    print("el valor minimo es: ", min(lista))
        
Insertar (lista)
Mostrar (lista)