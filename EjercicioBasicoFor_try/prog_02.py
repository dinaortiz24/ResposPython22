#Elabore un programa que lea 100 numeros y diga cual es el mayor
try:
    from re import X


    print("Ingresa una cadena de 100 numeros por favor")

    cont = 1
    mayor = 0
 
    for cont in range (1,11):
        print ("ingrese el numero: ", cont)
        num = int(input())
        x = num
        cont = cont + 1
        if x > mayor:
            mayor = x
        else:
            mayor = mayor
    print ("el numero mayor es ", mayor)
    
except:
    print("Ingrese un tipo de dato correcto")
    exit()
    