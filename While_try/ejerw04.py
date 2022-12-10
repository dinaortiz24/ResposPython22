# Elabore un programa en Python que lea n números enteros y determine cuántos de ellos son
# impares y cuál es su sumatoria.

try:
    print ("Cuantos numeros quieres analizar")
    n = int(input())
    i1 = n
    i2 = 0
    x = 0
    suma = 0

    while i1 != 0:
        x = i1 % 2 
        if x == 1:
           suma = suma + i1
           print (i1)
           i2 += 1
        i1 -= 1
    print ("la cantidad de numeros impares fue: ", i2)
    print ("la suma de los numeros impares es: ", suma)
except:
    print("ingrese datos numericos porfavor")
    print("el porgrama se cerrará")
    exit()