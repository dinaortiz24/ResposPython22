# calcular cateto adyacente dado hipotenusa y cateto opuesto
# Sigi
import math
print ("otorga el valor del cateto opuesto:")
co = float(input())
print ("otorga el valor de la hipotenusa:")
h = float(input())
phi = float(math.asin(co/h))
ca = float(h*math.cos(phi))
print ("el valor del cateto adyacente es:", ca)
print ("el valor del cateto adyacente es:", ca)
