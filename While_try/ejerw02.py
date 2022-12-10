# Elabore un programa en Python que calcule y muestre la sumatoria de los números enteros
# múltiplos de 5, comprendidos entre el 1 y n, es decir, 5 + 10 + 15 +.... + n.
try:    
    print ("ingresa numero final:")
    n = int(input())
    suma = 0
    mul = n/5
    i1 = 1
    while i1 <= mul:
        x = 5 * i1
        print(x)
        suma = suma + x
        i1 += 1
    
    print ("la sumatoria es:", suma)
except:
    print("Ingrese un numero porfavor, el programa se cerrará")
    exit()
    