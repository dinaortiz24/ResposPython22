# Elabore un programa en Python que imprima las tablas de multiplicar 
# del 1 a un número dado.
try:
    print ("hasta que tabla de numero deseas :")
    num = int(input())

    cont = 1
    cont2 = 1

    while cont <= num:
        cont2 = 1
        while cont2 <= 10:
            x =  cont * cont2
            print (cont, "x", cont2, "=", x)
            cont2 = cont2 + 1
        cont = cont + 1
        
except:
    print("Ingresó un dato no valido, vuelva a intentarlo")
    exit()
    