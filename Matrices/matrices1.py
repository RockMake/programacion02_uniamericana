print("mostrar todos los elementos de la matriz por fila")
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
for row in matrix:
    print(row)

print("mostrar todos los elementos de la matriz elemento a elemento en columnas")

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
for row in matrix:
    for colum in row:
        print(colum)

print("mostrar todos los elementows de la matriz en forma de matriz")
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
for row in matrix:
    for colm in row:
        print(colm, end=" ")
    print()
