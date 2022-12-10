# Elabore un programa en Python que muestre los números enteros en forma descendente de
# un número a otro dado. Los números se pueden dar en cualquier orden.
try:
    print ("¿Ingresa el numero de inicio: ")
    ni = float(input())
    print ("ingresa el numero final: ")
    nf = float (input())
    if ni < nf:
        aux = ni
        ni = nf
        nf = aux
    print ("lista ordenada: ")
    while ni >= nf:
        print (ni)
        ni-=1
except:
    print("Se ingreso un dato que no es correcto")
    exit()
    