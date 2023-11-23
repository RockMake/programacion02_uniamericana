# matriz = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9],]

# for i in matriz:
#     print(i)


def saludar(mensaje):
    print(mensaje)


saludar("hola mundo")
saludar("adios")


def suma(a, b):
    resultado = a + b
    return resultado


n = (input("ingrese un numero: "))
m = (input("ingrese otro numero: "))
resultado = suma(n, m)
print(resultado)
