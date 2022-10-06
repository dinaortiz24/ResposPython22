# Elabore un programa en Python que dada una cadena de texto, 
# indique el número de vocales que tiene.
cad = input ("dame la cadena:")
cont = 0
vocales=['a','e','i','o','u']
for vocal in cad:
    if vocal.lower() in vocales:
        cont+=1
        print (vocal)
print ("la cadena es %s" % cad + "tiene %d" % cont + "vocales" ) 