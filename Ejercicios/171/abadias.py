def abadias(V, N):

    maximo = 1
    resultado = 1
    i = N - 2
    maximo = V[N - 1]

    while i >= 0:
        if V[i] > maximo:
            maximo = V[i]
            resultado = resultado + 1
        i = i - 1

    return resultado


numPicos = 0
v = []
lecN = 0
fichero = open("./171/datos.txt")
contenido = fichero.read()
fichero.close()
lineas = contenido.splitlines()

for linea in lineas:
    valor = int(linea)  # convertir de cadena a número
    if lecN == 0:
        numPicos = valor
        lecN = 1
    else:
        v.append(valor)
print(abadias(v, numPicos))
