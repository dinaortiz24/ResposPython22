# 1 Elaborar un algoritmo en pseudocódigo o diagrama de flujo para que dadas la longitud
# de la hipotenusa y un cateto  adyacente de un triángulo rectángulo, calcule la longitud del otro
# cateto
# declaraciones
import math
cateto_o = 0.0
cateto_a = 0.0
print("Dame la longitud de la hipotenusa")
h = float(input())
print("Dame un cateto adyacente")
cateto_a = float(input())
x = cateto_a/h
cateto_o = math.sin(math.acos(x)) * h
print("El cateto opuesto es:", cateto_o)
