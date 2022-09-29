# programa que computa la cantidad de dinero, a partir de capital inicial
# el tipo de interés y el numero de años
print ("introduce el capital inicial:") 
ci = float(input())
print ("introduce la tasa de interes:")
ti = float(input())
print ("introduce el no. de años:")
ta = float(input())
cd = float(((ci)+((ci*ti/100)*ta)))
print ("la cantidad acumulada es:", cd)