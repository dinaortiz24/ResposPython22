# programa que almace los números que el usuario ingrese en una lista, terminar la inserción cuando el usuario
# ingrese “fin”, y utiliza las funciones max() y min() para calcular el máximo y el mínimo después
# de que el bucle termine.

import math
lista = []


def Insertar(lst):
    while (elem != 'fin'):
        elem = input("Ingresa el elemento ")
        if elem != 'fin':
            lst.append(int(elem))


def Mostrar(lst):
    print(lst)
    print("el valor maximo es: ", max(lista))
    print("el valor minimo es: ", min(lista))


Insertar(lista)
Mostrar(lista)
