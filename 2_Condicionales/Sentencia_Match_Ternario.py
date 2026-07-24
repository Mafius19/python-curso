# Ejercicio para practicar match-case y operador ternario

print("Calculadora de áreas")
print("1. Círculo")
print("2. Cuadrado")
print("3. Triángulo")
opcion = int(input("Elige una figura (1-3): "))

# Usando match-case (Python 3.10+)
match opcion:
    case 1:
        radio = float(input("Ingresa el radio del círculo: "))
        area = 3.1416 * radio ** 2
        print(f"El área del círculo es: {area:.2f}")
    case 2:
        lado = float(input("Ingresa el lado del cuadrado: "))
        # Usando operador ternario
        mensaje = "El área del cuadrado es positiva" if lado > 0 else "El lado debe ser positivo"
        print(mensaje)
        area = lado ** 2
        print(f"Área: {area:.2f}")
    case 3:
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        # Usando operador ternario para validación
        area = (base * altura) / 2 if base > 0 and altura > 0 else 0
        print(f"El área del triángulo es: {area:.2f}" if area > 0 else "La base y altura deben ser positivas")
    case _:
        print("Opción no válida")

# Ejemplo de operador ternario simple
es_valido = "válido" if opcion in [1, 2, 3] else "inválido"
print(f"La opción seleccionada fue {es_valido}")