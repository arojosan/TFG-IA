def fractal(l):
    resultado = 4
    if l > 1:
        resultado = 4 * l + 4*fractal(l / 2)
    return resultado


n = 0
v = []
lecN = 0
fichero = open("./167/datos.txt")
contenido = fichero.read()
fichero.close()
lineas = contenido.splitlines()
i = -1

for linea in lineas:
    valor = int(linea)  # convertir de cadena a número
    if lecN == 0:
        n = valor
        lecN = 1
    else:
        v.append(valor)
    print(fractal(v[i]))
    i += 1