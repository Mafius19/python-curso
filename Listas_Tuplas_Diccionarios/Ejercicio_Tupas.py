# ============================================
# EJERCICIO SIMPLE CON TUPLAS - PASO A PASO
# ============================================

print("=== EJERCICIO CON TUPLAS ===\n")

# ------------------------------------------------
# PASO 1: Crear una tupla
# ------------------------------------------------
print("PASO 1: Crear una tupla")
print("Las tuplas se crean con paréntesis () y son INMUTABLES (no pueden cambiar)\n")

# Crear una tupla con colores
colores = ("rojo", "azul", "verde", "amarillo")
print(f"Tupla creada: {colores}")
print(f"Tipo de dato: {type(colores)}")
print()

# ------------------------------------------------
# PASO 2: Acceder a elementos de la tupla
# ------------------------------------------------
print("PASO 2: Acceder a elementos por índice")
print("Los índices comienzan desde 0\n")

print(f"colores[0] = {colores[0]}")  # Primer elemento
print(f"colores[1] = {colores[1]}")  # Segundo elemento
print(f"colores[2] = {colores[2]}")  # Tercero elemento
print(f"colores[3] = {colores[3]}")  # Cuarto elemento
print()

# Índices negativos (desde el final)
print("También podemos usar índices negativos:")
print(f"colores[-1] = {colores[-1]}")  # Último elemento
print(f"colores[-2] = {colores[-2]}")  # Penúltimo elemento
print()

# ------------------------------------------------
# PASO 3: Obtener la longitud de la tupla
# ------------------------------------------------
print("PASO 3: Obtener la longitud de la tupla")
print(f"Longitud de la tupla: {len(colores)} elementos")
print()

# ------------------------------------------------
# PASO 4: Verificar si un elemento existe
# ------------------------------------------------
print("PASO 4: Verificar si un elemento existe en la tupla")

color_buscar = "azul"
if color_buscar in colores:
    print(f"✅ '{color_buscar}' SÍ está en la tupla")
else:
    print(f"❌ '{color_buscar}' NO está en la tupla")

color_buscar = "negro"
if color_buscar in colores:
    print(f"✅ '{color_buscar}' SÍ está en la tupla")
else:
    print(f"❌ '{color_buscar}' NO está en la tupla")
print()

# ------------------------------------------------
# PASO 5: Contar cuántas veces aparece un elemento
# ------------------------------------------------
print("PASO 5: Contar repeticiones de un elemento")

numeros = (1, 2, 3, 2, 4, 2, 5)
print(f"Tupla de números: {numeros}")
print(f"El número 2 aparece {numeros.count(2)} veces")
print()

# ------------------------------------------------
# PASO 6: Obtener el índice de un elemento
# ------------------------------------------------
print("PASO 6: Obtener el índice de un elemento")

indice = colores.index("verde")
print(f"El índice de 'verde' es: {indice}")
print()

# ------------------------------------------------
# PASO 7: Desempaquetar una tupla
# ------------------------------------------------
print("PASO 7: Desempaquetar una tupla")
print("Podemos asignar cada elemento de la tupla a una variable\n")

coordenadas = (10, 20, 30)
x, y, z = coordenadas
print(f"Tupla: {coordenadas}")
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")
print()

# ------------------------------------------------
# PASO 8: Slicing (obtener una porción de la tupla)
# ------------------------------------------------
print("PASO 8: Slicing - obtener una porción de la tupla")

letras = ("a", "b", "c", "d", "e", "f")
print(f"Tupla original: {letras}")
print(f"letras[1:4] = {letras[1:4]}")  # Desde índice 1 hasta 3
print(f"letras[:3] = {letras[:3]}")    # Desde inicio hasta índice 2
print(f"letras[3:] = {letras[3:]}")    # Desde índice 3 hasta el final
print()

# ------------------------------------------------
# PASO 9: Concatenar tuplas
# ------------------------------------------------
print("PASO 9: Concatenar tuplas")

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_combinada = tupla1 + tupla2
print(f"tupla1 = {tupla1}")
print(f"tupla2 = {tupla2}")
print(f"tupla1 + tupla2 = {tupla_combinada}")
print()

# ------------------------------------------------
# PASO 10: Tupla con un solo elemento
# ------------------------------------------------
print("PASO 10: Crear tupla con un solo elemento")
print("Importante: se necesita una coma al final\n")

no_tupla = (5)        # Esto NO es una tupla, es un entero
si_tupla = (5,)       # Esto SÍ es una tupla (nota la coma)

print(f"(5) = {no_tupla} - Tipo: {type(no_tupla).__name__}")
print(f"(5,) = {si_tupla} - Tipo: {type(si_tupla).__name__}")
print()

# ------------------------------------------------
# EJERCICIO PRÁCTICO PARA TI
# ------------------------------------------------
print("="*50)
print("EJERCICIO PRÁCTICO")
print("="*50)
print("Crea una tupla con tus 3 comidas favoritas")
print("Luego:")
print("1. Imprime la tupla completa")
print("2. Imprime tu comida favorita (primer elemento)")
print("3. Imprime la longitud de la tupla")
print("4. Verifica si 'pizza' está en tu tupla")
print("="*50)
