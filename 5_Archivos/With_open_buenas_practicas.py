"""
Vieja manera ya descarta por mala practica, ahora se usa el metodo with
archivo = open("archivo.txt", "w")
archivo.write("Hola mundo")
archivo.close()
"""

with open("archivo.txt", "w") as archivo:
    archivo.write("Hola mundo2")