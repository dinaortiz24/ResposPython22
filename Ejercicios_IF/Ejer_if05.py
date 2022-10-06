# Con base a la segunda ley de Newton (F=ma -Fuerza =masa por aceleración), 
# elaborar un programa en Python para que  pregunte si se desea calcular 
# la fuerza, masa o aceleración y según la opción seleccionada lea los 
# datos correspondientes y  muestre los resultados.
print ("Que deseas calcular...? 1 = Fuerza, 2 = masa, 3 = aceleración")
valor = float(input())
if valor == 1:
    print ("Proporciona el de la valor de masa:")
    m = float(input())
    print ("Otorga el valor de la aceleracion:")
    a = float(input())
    f = m*a
    print ("El valor de la fuerza es: ", f)
if valor == 2:
    print ("Proporciona el de la valor de fuerza:")
    f = float(input())
    print ("Otorga el valor de la aceleracion:")
    a = float(input())
    m = f/a
    print ("El valor de la masa es: ", m)
if valor == 3:
    print ("Proporciona el de la valor de fuerza:")
    f = float(input())
    print ("Otorga el valor de la masa:")
    m = float(input())
    a = f/m
    print ("El valor de la aceleración es: ", a)