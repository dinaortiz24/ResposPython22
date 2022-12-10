# Elabore un programa que permita la entrada de 100 numeros enteros 
# y determine cual de ellos es un numero primo
try:
    import random
    cont = 1
    primo = " "

    for cont in range (1,10):
        num = random.randint (1,100)
        x = num
        if x % 2 != 0:
            primo = primo + str(x) + " "
    print ("los numeros primos son: ", primo)
except:
    print("hay un dato que no es numerico, corregir por favor")