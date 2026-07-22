# ============================================
# OPERACIONES ARITMÉTICAS EN PYTHON
# ============================================

print("=== OPERACIONES ARITMÉTICAS ===\n")

# ------------------------------------------------
# FORMA 1: CON DATOS ESTABLECIDOS EN EL CÓDIGO
# ------------------------------------------------
print("--- Datos del código ---")

# Definimos variables con valores fijos
num1 = 15
num2 = 4

# Operaciones básicas
suma = num1 + num2          # Suma: 15 + 4 = 19
resta = num1 - num2         # Resta: 15 - 4 = 11
multiplicacion = num1 * num2  # Multiplicación: 15 * 4 = 60
division = num1 / num2      # División: 15 / 4 = 3.75
division_entera = num1 // num2  # División entera: 15 // 4 = 3
modulo = num1 % num2        # Módulo (resto): 15 % 4 = 3
potencia = num1 ** num2     # Potencia: 15 ** 4 = 50625

print(f"Números: {num1} y {num2}")
print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
print(f"División: {num1} / {num2} = {division}")
print(f"División entera: {num1} // {num2} = {division_entera}")
print(f"Módulo (resto): {num1} % {num2} = {modulo}")
print(f"Potencia: {num1} ** {num2} = {potencia}")

# ------------------------------------------------
# FORMA 2: CON DATOS DEL USUARIO (INPUT)
# ------------------------------------------------
print("\n--- Datos del usuario ---")

# Solicitar datos al usuario
# IMPORTANTE: input() siempre devuelve texto (string)
# Debemos convertir a número con int() o float()

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Operaciones con datos del usuario
suma_usuario = numero1 + numero2
resta_usuario = numero1 - numero2
multiplicacion_usuario = numero1 * numero2
division_usuario = numero1 / numero2

print(f"\nTus números: {numero1} y {numero2}")
print(f"Suma: {numero1} + {numero2} = {suma_usuario}")
print(f"Resta: {numero1} - {numero2} = {resta_usuario}")
print(f"Multiplicación: {numero1} * {numero2} = {multiplicacion_usuario}")
print(f"División: {numero1} / {numero2} = {division_usuario}")

# ------------------------------------------------
# EJEMPLO PRÁCTICO: CÁLCULO DE PROMEDIO
# ------------------------------------------------
print("\n--- Ejemplo práctico: Promedio de notas ---")

# Con datos del código
notas_codigo = [85, 92, 78, 90, 88]
promedio_codigo = sum(notas_codigo) / len(notas_codigo)
print(f"Notas (código): {notas_codigo}")
print(f"Promedio: {promedio_codigo}")

# Con datos del usuario
print("\nIngresa 3 notas para calcular el promedio:")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

promedio_usuario = (nota1 + nota2 + nota3) / 3
print(f"\nTus notas: {nota1}, {nota2}, {nota3}")
print(f"Tu promedio: {promedio_usuario}")

# ------------------------------------------------
# OPERADORES DE ASIGNACIÓN COMPUESTA
# ------------------------------------------------
print("\n--- Operadores de asignación compuesta ---")

contador = 10
print(f"Valor inicial: {contador}")

contador += 5   # Equivale a: contador = contador + 5
print(f"contador += 5 → {contador}")

contador -= 3   # Equivale a: contador = contador - 3
print(f"contador -= 3 → {contador}")

contador *= 2   # Equivale a: contador = contador * 2
print(f"contador *= 2 → {contador}")

contador /= 4   # Equivale a: contador = contador / 4
print(f"contador /= 4 → {contador}")
