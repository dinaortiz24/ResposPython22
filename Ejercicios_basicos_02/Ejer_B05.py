# Distancia euclidea entre dos puntos
import math
print ("otorga el valor de y2:")
y2 = float(input())
print ("otorga el valor de x2:")
x2 = float(input())
print ("otorga el valor de y1:")
y1 = float(input())
print ("otorga el valor de x1:")
x1 = float(input())
d1 = float(math.sqrt(((y2-y1)**2)+((x2-x1)**2)))
d = float(abs(d1))
print ("la distancia entre punto 1 y punto 2 es:", d)