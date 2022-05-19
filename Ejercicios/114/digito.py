def lastDig(N):

    resultado = 0
    
    if N == 0:
        resultado = 1
    elif N == 1:
        resultado = 1
    elif N == 2:
        resultado = 2
    elif N == 3:
        resultado = 6
    elif N == 4:
        resultado = 4
    return resultado


n = 0
lecN = 0
fichero = open("./114/datos.txt")
contenido = fichero.read()
fichero.close()
lineas = contenido.splitlines()

for linea in lineas:
    if lecN == 0:
        valor = int(linea)  # convertir de cadena a número
        lecN = 1
    n = int(linea)
    print(lastDig(n))
