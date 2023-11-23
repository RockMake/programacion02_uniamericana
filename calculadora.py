# importar libreria colorama para dar color a la consola
from colorama import Fore, Style
import colorama
colorama.init()
print(Fore.GREEN + "________________________________________")
nombre = input(Fore.BLACK + "cual es tu nombre: ")
print(Fore.BLUE + f"Hola {nombre} Bienvenido a mi calculadora")
print(Fore.GREEN + "________________________________________")

# Funciones para realizar las operaciones matemáticas básicas


def menu():
    print(f"""{Fore.GREEN}
    ***********************************
    *          CALCULADORA            *
    ***********************************
      Opciones disponibles: 
      1. {Fore.CYAN}Sumar +  {Fore.GREEN}                   
      2. {Fore.CYAN}Restar - {Fore.GREEN}                    
      3. {Fore.CYAN}Multiplicar * {Fore.GREEN}              
      4. {Fore.CYAN}Dividir / {Fore.GREEN}                           
      0. {Fore.RED}Salir{Fore.GREEN}                                           
    ***********************************{Style.RESET_ALL}"""
          )
    print(Fore.GREEN + "________________________________________")


def sumar(n1, n2):
    resultado = n1 + n2
    if resultado == int(resultado):
        resultado = int(resultado)
        n1 = int(n1)
        n2 = int(n2)
    print(Fore.MAGENTA +
          f""" 
        Resultado
        {n1} + {n2} = {resultado}""")


def restar(n1, n2):
    resultado = n1 - n2
    if resultado == int(resultado):
        resultado = int(resultado)
        n1 = int(n1)
        n2 = int(n2)
    print(Fore.MAGENTA +
          f""" 
        Resultado
        {n1} - {n2} = {resultado}""")


def multiplicar(n1, n2):
    resultado = n1 * n2
    if resultado == int(resultado):
        resultado = int(resultado)
        n1 = int(n1)
        n2 = int(n2)
    print(Fore.MAGENTA +
          f""" 
        Resultado
        {n1} * {n2} = {resultado}""")


def dividir(n1, n2):
    if n2 == 0:
        print(Fore.RED + "no se puede dividir entre 0")
    else:
        resultado = n1 / n2
        if resultado == int(resultado):
            resultado = int(resultado)
            n1 = int(n1)
            n2 = int(n2)
        print(Fore.MAGENTA +
              f""" 
            Resultado
            {n1} / {n2} = {resultado}""")


def potenciacion(n1, n2):
    resultado = n1 ** n2
    if resultado == int(resultado):
        resultado = int(resultado)
        n1 = int(n1)
        n2 = int(n2)
    print(Fore.CYAN +
          f"""{n1}^{n2}, el resultado es: {resultado}""")


while True:  # Bucle principal
    menu()
    while True:
        # Solicitar al usuario que ingrese el operador deseado
        op = input(
            f"ingrese el operador {Fore.CYAN}(+ - * / ^): ").lower()
        # Si el usuario ingresa "salir" o "0", salir del bucle
        if op == "salir" or op == "0":
            break
        n1 = None
        n2 = None
        # Solicitar al usuario el primer valor hasta que ingrese un número válido
        while n1 is None:
            valor = input(Fore.BLUE + "ingresa primer valor: ")
            vPrueba = valor
            vPrueba = vPrueba.replace(".", "")
            if (vPrueba.startswith("-")):
                vPrueba = vPrueba.replace("-", "")
            if vPrueba.isdigit():
                n1 = float(valor)
            else:
                print(Fore.RED + "ingrese un numero valido")
                continue

        # Solicitar al usuario el segundo valor hasta que ingrese un número válido
        while n2 is None:
            valor = input(Fore.BLUE + "ingresa segundo valor: ")
            vPrueba = valor
            vPrueba = vPrueba.replace(".", "")
            if (vPrueba.startswith("-")):
                vPrueba = vPrueba.replace("-", "")
            if vPrueba.isdigit():
                n2 = float(valor)
            else:
                print(Fore.RED + "ingrese un numero valido")
                continue
        # Realizar la operación solicitada por el usuario
        if op == "sumar" or op == "1" or op == "+":
            sumar(n1, n2)

        elif op == "restar" or op == "2" or op == "-":
            restar(n1, n2)

        elif op == "multiplicar" or op == "3" or op == "*":
            multiplicar(n1, n2)

        elif op == "dividir" or op == "4" or op == "/":
            dividir(n1, n2)

        elif op == "potenciacion" or op == "5" or op == "^" or op == "**":
            potenciacion(n1, n2)

        else:
            print(Fore.RED + "operador incorrecto.")
        print(Fore.GREEN + "________________________________________")
        fin = input(Fore.CYAN + "desea realizar otra operacion? (s/n) ").lower()

        if fin == "n":
            break
        print(Fore.GREEN + "________________________________________ ")

    print(Fore.GREEN + f"chao {nombre} gracias por usar mi calculadora")
    break
