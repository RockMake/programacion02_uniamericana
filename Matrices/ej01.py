Filas = int(input("cuantas filas tiene la matriz ?: "))
colum = int(input("cuantas columnas tiene la matriz ?: "))
matriz = []

for row in range(Filas):
    filaas = []  # agrega la cantidad de filas
    for col in range(colum):
        filaas.append(
            int(input(f"ingresa el valor de la fila {row}, :  columna {col}: ")))
    # guardas los elementos de cada filas dentro de la matriz
    matriz.append(filaas)


for row in matriz:  # imprime la matiz en forma de matriz
    for colm in row:
        print(colm, end=" ")
    print()

