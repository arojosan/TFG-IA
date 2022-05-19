def insercion(V, N):

    for i in range(N) :
        x=V[i];
        j=i-1;
        while j >= 0 and V[j] > x : ## va desplazando hacia la derecha los v[j] hasta encontrar un v[j] < v[i]
            V[j+1] = V[j];
            j=j-1;
            V[j + 1] = x; ## inserta el v[i]

n = 0
v = []
lecN = 0
fichero = open("./323/datos.txt")
contenido = fichero.read()
fichero.close()
lineas = contenido.splitlines()

for linea in lineas:
    valor = int(linea)  # convertir de cadena a número
    if lecN == 0:
        n = valor
        lecN = 1
    else:
        v.append(valor)
insercion(v, n)