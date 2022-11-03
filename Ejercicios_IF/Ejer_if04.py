# Elaborar un programa en Python para que lea tres números diferentes y diga cuál es el mayor de los tres.
print ("dame el primer numero:")
a = float(input())
print ("dame el segundo numero:")
b = float(input())
print ("dame el segundo número:")
c = float(input())
if a>b and a>c:
    print ("el número", a, "es mayor")
if b>a and b>c:
    print ("el número", b, "es mayor")
if c>a and c>b:
    print ("el número", c, "es mayor")
           