# Ejemplo completo de inputs en Python

print("=== Formulario de Datos ===\n")

# Input de texto (string)
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")

# Input de número entero con manejo de errores
while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        if edad > 0 and edad < 120:
            break
        else:
            print("Edad no válida, intenta de nuevo.")
    except ValueError:
        print("Debes ingresar un número entero.")

# Input de número decimal
altura = float(input("Ingresa tu altura en metros: "))

# Input booleano (convertido de texto)
while True:
    es_estudiante = input("¿Eres estudiante? (s/n): ").lower()
    if es_estudiante in ['s', 'n']:
        es_estudiante = (es_estudiante == 's')
        break
    print("Responde con 's' o 'n'.")

# Cálculos con los datos
año_nacimiento = 2026 - edad
nombre_completo = f"{nombre} {apellido}"

# Mostrar resultados formateados
print("\n=== Resultados ===")
print(f"Nombre completo: {nombre_completo}")
print(f"Edad: {edad} años")
print(f"Año de nacimiento aproximado: {año_nacimiento}")
print(f"Altura: {altura} metros")
print(f"Es estudiante: {'Sí' if es_estudiante else 'No'}")

# Operación adicional
print(f"\nEn 10 años tendrás {edad + 10} años")