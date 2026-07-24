# ============================================
# ESTRUCTURAS DE CONTROL EN PYTHON
# ============================================

print("=== ESTRUCTURAS DE CONTROL EN PYTHON ===\n")

# ------------------------------------------------
# 1. IF - Ejecuta código si una condición es verdadera
# ------------------------------------------------
print("--- 1. IF (Condición simple) ---")

edad = 18

if edad >= 18:
    print("✅ Eres mayor de edad")
    print("   Puedes votar y conducir")

if edad < 18:
    print("❌ Eres menor de edad")

print()

# ------------------------------------------------
# 2. ELIF - Evalúa otra condición si la anterior fue falsa
# ------------------------------------------------
print("--- 2. ELIF (Múltiples condiciones) ---")

nota = 85

if nota >= 90:
    print("✅ Calificación: A (Excelente)")
elif nota >= 80:
    print("✅ Calificación: B (Muy bien)")
elif nota >= 70:
    print("✅ Calificación: C (Bien)")
elif nota >= 60:
    print("✅ Calificación: D (Suficiente)")
else:
    print("❌ Calificación: F (Reprobado)")

print()

# ------------------------------------------------
# 3. ELSE - Ejecuta si ninguna condición anterior fue verdadera
# ------------------------------------------------
print("--- 3. ELSE (Caso por defecto) ---")

numero = 7

if numero % 2 == 0:
    print(f"✅ {numero} es un número PAR")
else:
    print(f"✅ {numero} es un número IMPAR")

print()

# Ejemplo completo con if-elif-else
print("Ejemplo: Clasificar temperatura")
temperatura = 25

if temperatura > 30:
    print("🔥 Hace mucho calor")
elif temperatura > 20:
    print("☀️ Hace calor agradable")
elif temperatura > 10:
    print("🌤️ Hace fresco")
else:
    print("❄️ Hace frío")

print()

# ------------------------------------------------
# 4. FOR - Repite código sobre una secuencia
# ------------------------------------------------
print("--- 4. FOR (Bucle sobre secuencia) ---")

# Iterar sobre una lista
frutas = ["manzana", "banana", "naranja", "uva"]
print("Iterar sobre lista de frutas:")
for fruta in frutas:
    print(f"   - {fruta}")

print()

# Iterar con range()
print("Iterar con range(1, 6):")
for i in range(1, 6):
    print(f"   Número: {i}")

print()

# Iterar sobre un string
print("Iterar sobre un string:")
texto = "Python"
for letra in texto:
    print(f"   Letra: {letra}")

print()

# ------------------------------------------------
# 5. WHILE - Repite código mientras una condición sea verdadera
# ------------------------------------------------
print("--- 5. WHILE (Bucle condicional) ---")

# Ejemplo: Contador regresivo
print("Contador regresivo:")
contador = 5
while contador > 0:
    print(f"   {contador}...")
    contador -= 1
print("   ¡Despegue! 🚀")

print()

# Ejemplo: Validación de input
print("Validación de contraseña:")
while True:
    contraseña = input("Ingresa 'secreto' para continuar: ")
    if contraseña == "secreto":
        print("✅ Contraseña correcta")
        break
    else:
        print("❌ Contraseña incorrecta, intenta de nuevo")

print()

# ------------------------------------------------
# 6. TRY-EXCEPT - Manejo de errores
# ------------------------------------------------
print("--- 6. TRY-EXCEPT (Manejo de errores) ---")

# Ejemplo: División con manejo de error
print("División con manejo de división por cero:")
try:
    numerador = 10
    denominador = 0
    resultado = numerador / denominador
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("❌ Error: No se puede dividir por cero")

print()

# Ejemplo: Conversión con manejo de error
print("Conversión de texto a número:")
try:
    texto = "abc"
    numero = int(texto)
    print(f"Número: {numero}")
except ValueError:
    print(f"❌ Error: '{texto}' no se puede convertir a entero")

print()

# Ejemplo: Múltiples excepciones
print("Múltiples tipos de errores:")
try:
    lista = [1, 2, 3]
    print(lista[10])  # Índice fuera de rango
except IndexError:
    print("❌ Error: Índice fuera de rango")
except Exception as e:
    print(f"❌ Error general: {e}")

print()

# ------------------------------------------------
# 7. WITH - Gestor de contexto
# ------------------------------------------------
print("--- 7. WITH (Gestor de contexto) ---")

# Ejemplo: Lectura de archivo (simulado)
print("Ejemplo de with para archivos:")
print("   with open('archivo.txt', 'r') as archivo:")
print("       contenido = archivo.read()")
print("   # El archivo se cierra automáticamente")
print("   # Incluso si ocurre un error")

print()

# ------------------------------------------------
# 8. MATCH-CASE - Pattern matching (Python 3.10+)
# ------------------------------------------------
print("--- 8. MATCH-CASE (Pattern matching) ---")

# Ejemplo: Clasificar día de la semana
dia = "lunes"

match dia.lower():
    case "lunes":
        print("📅 Día 1 de la semana")
    case "martes":
        print("📅 Día 2 de la semana")
    case "miércoles":
        print("📅 Día 3 de la semana")
    case "jueves":
        print("📅 Día 4 de la semana")
    case "viernes":
        print("📅 Día 5 de la semana")
    case "sábado" | "domingo":
        print("🎉 Fin de semana")
    case _:
        print("❌ Día no reconocido")

print()

# Ejemplo con números
print("Clasificar número:")
numero = 3

match numero:
    case 1:
        print("Primero")
    case 2:
        print("Segundo")
    case 3:
        print("Tercero")
    case _:
        print("Otro número")

print()

# ------------------------------------------------
# RESUMEN
# ------------------------------------------------
print("="*50)
print("RESUMEN DE ESTRUCTURAS DE CONTROL")
print("="*50)
print("1. if     - Ejecuta si condición es verdadera")
print("2. elif   - Evalúa otra condición si anterior fue falsa")
print("3. else   - Ejecuta si ninguna condición fue verdadera")
print("4. for    - Repite sobre una secuencia")
print("5. while  - Repite mientras condición sea verdadera")
print("6. try    - Intenta ejecutar código que podría fallar")
print("7. except - Captura y maneja errores")
print("8. with   - Gestor de contexto (cierra recursos automáticamente)")
print("9. match/case - Pattern matching (Python 3.10+)")
print("="*50)