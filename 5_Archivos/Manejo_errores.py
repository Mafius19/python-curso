"""
ZeroDivisionError: se activa cuando divides entre 0
ValueError: Se activa cuando conviertes un dato invalido (string ->x int)
FileNotFoundError: Se activa cuando accedemos a un archivo inexistente
TypeError: Se activa cuando usamos tipos incompatible("texto" + 5)
IndexError: Se activa cuando accedes a una posicion fuera de una lista.


"""

try:
    numero = int(input("Ingresa un numero "))
    resultado = 10 / numero
    print(f"\n El resultado de la division 10 / {numero} es : {resultado}")

except ZeroDivisionError:
    print(f"El numero {numero} no es divisible (es un numero 0)")

except ValueError:
    print(f"Porfavor ingresa un numero, valor ingresado")