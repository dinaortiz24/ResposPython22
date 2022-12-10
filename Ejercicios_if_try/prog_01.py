# 1.- Elaborar un programa en Python para calcular el sueldo de un empleado
# con base a las horas trabajadas y se le otorga un
# incentivo del 5% si trabajó más de 40 horas.
try:
    ph = 30

    print ("horas trabajadas durante la semana del empleado:")
    ht = float(input())

    if ht > 40:
        ht = (ht * ph)*1.05
    else:
        ht = (ht*ph)
        print ("el sueldo semanal del trabajdor es:", ht)
except: 
    print ("tecleaste una letra, se cerrará programa.")