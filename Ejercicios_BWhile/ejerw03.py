# Elabore un programa en Python que calcule e imprima el factorial de un número dado.
print ("Ingresa el numero que deseas tener el factorial")
n1 = int(input())
n2 = n1
fact = 1

if n1 != 1 or n1 !=0:
    while n2 > 1:
       fact = fact * n2 
       n2 -=1                 
    print ("el factorial del numero", n1, "es: ", fact)

else: 
    print ("el factorial del numero", n1, "es: ", fact)
    
   