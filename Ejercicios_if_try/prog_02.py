# Elaborar un programa en Python para que solicite al usuario como 
# dato de entrada una calificación y muestre una leyenda
# según la siguiente tabla:
# ◦ 10 Excelente
# ◦ 9 Muy bien
# ◦ 8 Bien
# ◦ 7 Regular
# ◦ 6 Mal
# ◦ 5 a 0 Muy mal
try:
    print ("Que calificación obtvo el alumno Chaparrito Chuacheneguer:")
    cal=float(input())
    if cal <= 5:
        print ("Muy mal")
    if cal == 6:
        print ("Mal")
    if cal == 7:
        print ("Regular")
    if cal == 8:
        print ("Bien")
    if cal == 9:
        print ("Muy Bien")
    if cal == 10:
        print ("Excelente")
except:
    print ("calificacion no válida, intente nuevamente")