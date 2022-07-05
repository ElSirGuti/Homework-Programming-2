"""
a) Lea un número N (entero), determine y escriba el factorial de N, 
si este es positivo, de lo contrario escriba el mensaje 
"el numero es negativo". 
"""
#declaramos la funcion que es la del factorial
def factorial(n):
    #estas son las condiciones para el factorial
    #donde si n es 0 o 1 el resultado sera 1
    if n == 0 or n == 1:
        resultado = 1
    #Luego otra condicion donde si n es menor que 0 va a devolver
    #un valor que es el texto
    elif n < 0:
        #esto es lo que devuelve return es devolver en spanish
        return "El numero es negativo"
    #la ultima condicion es con un numero mayor a 1 y se usa la formula
    #para hallar el factorial
    elif n > 1:
        resultado = n * factorial(n-1)
    #otra vez return pero este tiene que estar identado al mismo nivel
    #que el elif
    return resultado

#declaramos la funcion main() que significa principal y es la que
#ejecutara el programa
def main():
    #la variable res le solicita al usuario un valor
    res = int(input("Introduce un numero: "))
    #la variable xd toma el numero introducido en res y res
    #pasaria a ser n en la funcion factorial()
    #algo asi como res = n
    xd = factorial(res)
    #imprimimos el resultado que se almacenara en la variable xd
    #que es la que ejecuta la funcion factorial()
    print(xd)
#se ejecuta la funcion main()
main()

""" Por que se ejecuta primero la funcion main() en vez de factorial() que esta de primero en el codigo?
Bueno para llamar a una funcion y que se ejecute necesitas aparte de declararla por ejemplo 'def funcion():'
pones luego de eso 'funcion()' que hara que se ejecute la funcion
entonces se ejecuta main() y luego factorial() porque factorial() esta contenida dentro de main()
"""