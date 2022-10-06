# 1. - Elabore un programa en Python que dada una cadena de texto, indique el número de vocales
# que tiene.
cadena = input("Dame la cadena \n")
contador = 0
vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in cadena:
    if vocal.lower() in vocales:
        contador += 1
        print(vocal)
print("La cadena es %s" % cadena + " tiene %d " % contador + " vocales")
