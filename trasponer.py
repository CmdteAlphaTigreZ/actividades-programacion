# Procedimiento que traspone una matriz
# Autor: Santiago Pinto             Fecha: 2022-08-13

# Nota: por ahora sólo sirve con matrices cuadradas.
def trasponer(matriz):
    cant_filas = len(matriz)
    if cant_filas != 0:
        cant_columnas = len(matriz[0])
    else:
        return
    for i in range(cant_filas):
        for j in range(0, i):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]
