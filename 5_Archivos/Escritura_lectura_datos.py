"""
Modos de apertura comunes:
'r': Lectura (por defecto)
'w': Escritura (sobrescribe el archivo si existe)
'a': Añadir al final del archivo
'x': Creación exclusiva (falla si el archivo ya existe)
'b': Modo binario
'+': Actualización (lectura y escritura)


Estructura:

with open("nombre_archivo", "modo_apertura") as archivo:
    
"""

with open('mi_primer_archivo.txt','r') as archivo:
    # archivo.write("Hola, soy un archivo creado en python")
    # archivo.write("\nbienvenido a mi curso de python")
    # archivo.close()
    
    # archivo.write("\nSoy una linea agregada con el modo a")
    # archivo.close()

    contenido = archivo.read()
    print(contenido)


 
