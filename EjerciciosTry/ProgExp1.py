import sys
i = 0
try:

    f = open('myfile.txt')

    s = f.readline(10)
    f.truncate()
    s = f.readline(10)
    i = int(s.strip())

# 3except OSError as err:
  #  print("OS error: {0}".format(err))

# except ValueError:
 #   print("no se puede covnertir a entero")
except BaseException as err:
    print("No se identificó el error {err=}, {type(err)=}")
    raise
print(i)
i = i+2
s = s+"hola"
print(i)
print(s)
