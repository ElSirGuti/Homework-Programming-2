"""
4. Programar un procedimientos que calcule los números primos entre dos números que sean introducidos por el usuario
"""

def esprimo():
    print("====Calcular número primo====")
    a = int(input("Ingrese un número: "))
    b = int(input("Ingrese un segundo número: "))
    cont = 0

    if a > b:
        primero = b
        segundo = a
    else:
        primero = a
        segundo = b

    cont += primero

    while cont < segundo:
        nprimo = True
        for i in range(2, cont):
            if (cont %  i) == 0:
                nprimo = False
        if nprimo:
            print(cont)
        cont += 1

def main():
    esprimo()

main()