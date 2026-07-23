"""
 Ejercicio: Registro de varios estudiantes y consulta de información

Objetivo:
-Crear un diccionario para varios estudiantes.

-Almacenar los datos de cada estudiante dentro del diccionario.

-Mostrar todos los estudiantes registrados.

-Consultar los datos de un estudiante por su nombre.

Enunciado:

-Crea un diccionario llamado estudiantes.

-Dentro del diccionario, cada clave será el nombre del estudiante.

-Cada valor será otro diccionario con:
- "Nombre"

-"edad"

-"curso"

-"inscrito" (valor booleano)

-Muestra todos los nombres registrados.

-Permite al usuario ingresar el nombre de un estudiante y muestra sus datos.


#CODIGO SOLUCION PROPIA


estudiantes = {}

estudiantes["Ana"]= {

    "Nombre": "Ana",
    "Edad": 22,
    "Curso": "Python",
    "Inscrito": True
}   

estudiantes["Luis"] ={

    "Nombre": "Luis",
    "Edad": 25,
    "Curso": "Python",
    "Inscrito": True
}

estudiantes["Sofía"]={

    "Nombre": "Sofía",
    "Edad": 22,
    "Curso": "Python",
    "Inscrito": True
}

print("===== Estudiantes Registrados. =====")

for nombre in estudiantes:
    print("-",nombre)

nombre_consulta = input(" Escribe el nombre del estudiante para ver sus datos:  ")

if nombre_consulta in estudiantes:
    print("Informacion de : ", nombre_consulta)
    print("Edad: ", estudiantes[nombre_consulta]["Edad"])
    print("Curso: ",estudiantes[nombre_consulta]["Curso"])
    print("Inscrito: ",estudiantes[nombre_consulta]["Inscrito"])
else:
    print("El estudiante ingresado no esta registrado en la base de datos.")
    print("Vuelve a intentarlo mas tarde.") 
"""





# Base de datos de estudiantes
estudiantes = {
    "Ana": {
        "Nombre": "Ana",
        "Edad": 22,
        "Curso": "Python",
        "Inscrito": True
    },
    "Luis": {
        "Nombre": "Luis",
        "Edad": 25,
        "Curso": "Python",
        "Inscrito": True
    },
    "Sofía": {
        "Nombre": "Sofía",
        "Edad": 22,
        "Curso": "Python",
        "Inscrito": True
    }
}

while True:
    # Mostrar lista de estudiantes
    print("\n" + "="*50)
    print("ESTUDIANTES REGISTRADOS".center(50))
    print("="*50)
    for nombre in sorted(estudiantes.keys()):
        print(f"- {nombre}")
    print("="*50 + "\n")
    
    # Pedir nombre del estudiante
    nombre_consulta = input("Escribe el nombre del estudiante (o 'salir' para terminar): ").strip()
    
    # Opción para salir del programa
    if nombre_consulta.lower() == 'salir':
        print("\n¡Hasta luego!")
        break
    
    # Buscar estudiante (insensible a mayúsculas)
    estudiante_encontrado = None
    for nombre in estudiantes:
        if nombre.lower() == nombre_consulta.lower():
            estudiante_encontrado = nombre
            break
    
    # Mostrar resultado
    if estudiante_encontrado:
        print("\n" + "="*50)
        print(f"INFORMACIÓN DE: {estudiante_encontrado.upper()}".center(50))
        print("="*50)
        print(f"Edad:    {estudiantes[estudiante_encontrado]['Edad']} años")
        print(f"Curso:   {estudiantes[estudiante_encontrado]['Curso']}")
        print(f"Inscrito: {'Sí' if estudiantes[estudiante_encontrado]['Inscrito'] else 'No'}")
        print("="*50)
    else:
        print(f"\n❌ El estudiante '{nombre_consulta}' no está registrado.")
        print("Por favor, intenta con otro nombre.")
    
    # Pausa antes de limpiar la pantalla
    input("\nPresiona Enter para continuar...")
    # Limpiar pantalla (alternativa simple)
    print("\n" * 100)
