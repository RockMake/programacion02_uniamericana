matriz_a = [[1, 3, 4],
            [2, 5, 6],
            [1, 2, 3]]
matriz_b = [[3, 4, 6],
            [4, 2, 6],
            [9, 1, 6]]
matriz_c = []


for fila in range(len(matriz_a)):
    fila_nueva = []  # crea una lista para guardar temporalmente la suma de las matrices
    for col in range(len(matriz_a[0])):
        fila_nueva.append(matriz_a[fila][col] +
                          matriz_b[fila][col])  # suma las matrices
    matriz_c.append(fila_nueva)

for i in matriz_c:
    print(i)
