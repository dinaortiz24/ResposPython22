# Elaborar un algoritmo en pseudocódigo o diagrama de flujo para calcular e imprimir
# el precio de venta de un artículo que se calcula añadiéndole al costo de producción 
# el 120% de utilidad y el 16% de impuesto.
print ("¿Que costo de producción del articulo se tiene?")
cp=float(input())
# calculamos la utilidad:
u = ((cp*120)/100)
# calculamos el impuesto:
imp = ((cp*16)/100)
# calculamos el precio de venta:
pv = (cp+u+imp)
print ("el precio de venta del artículo sería:", pv)