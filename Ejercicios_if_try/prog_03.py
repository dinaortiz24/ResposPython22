# De acuerdo con la clase de sus ángulos, los triángulos se clasifican en:
# Rectángulo: tiene un ángulo recto (igual a 90°)
# Obtusángulo: tiene un ángulo obtuso (mayor a 90° pero menor que 180°)
# Acutángulo: los tres ángulos son agudos (menores que 90°)
try:
    print ("dame el valor del primer angulo A")
    A = float(input())
    print ("dame el valor del primer angulo B")
    B = float(input())
    print ("dame el valor del primer angulo C")
    C = float(input())
    if A == 90 or B == 90 or C == 90:
        print ("El triangulo es rectangulo")
    elif A < 180 and A > 90 or B < 180 and B > 90 or C < 180 and C >90:
        print ("el triángulo es obtusangulo")
    else:
        print ("El triangulo es acutangulo") 
except:
    print ("Se ingreso un dato incorrecto")