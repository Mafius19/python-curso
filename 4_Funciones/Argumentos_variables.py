"""
*args : argumentos posicionales, estos guardan la informacion es una tupla
*kwargs: son argumentos clave-valor guarda la informacion como un diccionario

"""

#Argumentos args
def saludar(*args):
    print("Bienvenidos a el curso de python")
    for saludo in args:
        print(f"bienvenido: {saludo}")



print("Ejemplo de args")
saludar("Kevin","Sofia","Peter")

#argumentos kwargs: clave-valor

def mostrar_datos(**kwargs):
    print(f"La informacion del usuario es: {kwargs}")

print("Ejemplo de kwargs")
mostrar_datos(Nombre="Kevin",Edad=22,Genero="Masculino")