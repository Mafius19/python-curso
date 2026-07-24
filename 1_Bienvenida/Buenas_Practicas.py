# ============================================
# BUENAS PRÁCTICAS PARA DECLARACIÓN DE VARIABLES EN PYTHON
# ============================================

print("=== BUENAS PRÁCTICAS DE VARIABLES ===\n")

# ------------------------------------------------
# 1. USAR NOMBRES DESCRIPTIVOS Y CLAROS
# ------------------------------------------------
print("--- 1. Nombres descriptivos ---")

# ❌ MAL: Nombres confusos o cortos
x = 25
d = 10.5
n = "Juan"

# ✅ BIEN: Nombres que explican qué contiene la variable
edad = 25
altura = 10.5
nombre = "Juan"

print(f"✅ edad = {edad} (claro qué representa)")
print(f"✅ altura = {altura} (claro qué representa)")
print(f"✅ nombre = '{nombre}' (claro qué representa)")

# ------------------------------------------------
# 2. USAR snake_case (minúsculas con guiones bajos)
# ------------------------------------------------
print("\n--- 2. Usar snake_case ---")

# ❌ MAL: CamelCase o PascalCase
nombreUsuario = "Juan"
PrecioProducto = 100
NumeroTelefono = 123456789

# ✅ BIEN: snake_case (convención de Python)
nombre_usuario = "Juan"
precio_producto = 100
numero_telefono = 123456789

print(f"✅ nombre_usuario = '{nombre_usuario}'")
print(f"✅ precio_producto = {precio_producto}")
print(f"✅ numero_telefono = {numero_telefono}")

# ------------------------------------------------
# 3. EVITAR PALABRAS RESERVADAS DE PYTHON
# ------------------------------------------------
print("\n--- 3. Evitar palabras reservadas ---")

# ❌ MAL: Usar palabras reservadas de Python
# class = "Matemáticas"  # 'class' es reservada
# def = 10              # 'def' es reservada
# return = "Hola"       # 'return' es reservada
# import = 5            # 'import' es reservada

# ✅ BIEN: Usar alternativas descriptivas
materia = "Matemáticas"
cantidad = 10
saludo = "Hola"
valor_importado = 5

print(f"✅ materia = '{materia}' (evita 'class')")
print(f"✅ cantidad = {cantidad} (evita 'def')")
print(f"✅ saludo = '{saludo}' (evita 'return')")

# Lista de palabras reservadas en Python:
palabras_reservadas = [
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
    'while', 'with', 'yield'
]
print(f"\nPalabras reservadas a evitar: {palabras_reservadas}")

# ------------------------------------------------
# 4. INICIALIZAR VARIABLES CON VALORES APROPIADOS
# ------------------------------------------------
print("\n--- 4. Inicialización apropiada ---")

# ❌ MAL: Dejar variables sin inicializar o con valores incorrectos
# contador  # Error si se usa sin asignar
# precio = "100"  # String cuando debería ser número

# ✅ BIEN: Inicializar con el tipo correcto
contador = 0
precio = 100.0
activo = True
mensaje = ""

print(f"✅ contador = {contador} (inicializado en 0)")
print(f"✅ precio = {precio} (tipo float)")
print(f"✅ activo = {activo} (tipo boolean)")
print(f"✅ mensaje = '{mensaje}' (string vacío)")

# ------------------------------------------------
# 5. USAR CONSTANTES EN MAYÚSCULAS
# ------------------------------------------------
print("\n--- 5. Constantes en mayúsculas ---")

# ✅ BIEN: Constantes (valores que no cambian) en MAYÚSCULAS
PI = 3.14159
GRAVEDAD = 9.81
MAX_INTENTOS = 3
URL_BASE = "https://api.ejemplo.com"

print(f"✅ PI = {PI} (constante)")
print(f"✅ GRAVEDAD = {GRAVEDAD} (constante)")
print(f"✅ MAX_INTENTOS = {MAX_INTENTOS} (constante)")
print(f"✅ URL_BASE = '{URL_BASE}' (constante)")

# ------------------------------------------------
# 6. SER CONSISTENTE EN EL NOMBRAMIENTO
# ------------------------------------------------
print("\n--- 6. Consistencia en el nombramiento ---")

# ❌ MAL: Mezclar estilos
usuario_nombre = "Juan"
usuarioApellido = "Perez"
UsuarioEdad = 25

# ✅ BIEN: Mantener un patrón consistente
usuario_nombre = "Juan"
usuario_apellido = "Perez"
usuario_edad = 25

print(f"✅ usuario_nombre = '{usuario_nombre}'")
print(f"✅ usuario_apellido = '{usuario_apellido}'")
print(f"✅ usuario_edad = {usuario_edad}")

# ------------------------------------------------
# 7. EVITAR CARACTERES ESPECIALES Y NÚMEROS AL INICIO
# ------------------------------------------------
print("\n--- 7. Evitar caracteres especiales ---")

# ❌ MAL: Caracteres no permitidos
# 1nombre = "Juan"      # No puede empezar con número
# nombre-usuario = "Juan" # Guion no permitido (usa guion bajo)
# nombre@usuario = "Juan" # Arroba no permitida
# class = "Matemáticas"  # Palabra reservada

# ✅ BIEN: Solo letras, números y guiones bajos
nombre1 = "Juan"
nombre_usuario = "Juan"
nombre_usuario_2 = "Maria"

print(f"✅ nombre1 = '{nombre1}'")
print(f"✅ nombre_usuario = '{nombre_usuario}'")
print(f"✅ nombre_usuario_2 = '{nombre_usuario_2}'")

# ------------------------------------------------
# 8. USAR TIPOS DE DATOS APROPIADOS
# ------------------------------------------------
print("\n--- 8. Tipos de datos apropiados ---")

# ✅ BIEN: Elegir el tipo correcto para cada dato
edad = 25                    # int para números enteros
precio = 99.99               # float para números con decimales
nombre = "Juan"              # str para texto
es_activo = True             # bool para verdadero/falso
notas = [85, 90, 78]         # list para colecciones
datos = {"nombre": "Juan", "edad": 25}  # dict para pares clave-valor

print(f"✅ edad = {edad} (tipo: {type(edad).__name__})")
print(f"✅ precio = {precio} (tipo: {type(precio).__name__})")
print(f"✅ nombre = '{nombre}' (tipo: {type(nombre).__name__})")
print(f"✅ es_activo = {es_activo} (tipo: {type(es_activo).__name__})")
print(f"✅ notas = {notas} (tipo: {type(notas).__name__})")
print(f"✅ datos = {datos} (tipo: {type(datos).__name__})")

# ------------------------------------------------
# 9. AGRUPAR VARIABLES RELACIONADAS
# ------------------------------------------------
print("\n--- 9. Agrupar variables relacionadas ---")

# ✅ BIEN: Variables relacionadas juntas
# Datos de un usuario
usuario_nombre = "Juan"
usuario_apellido = "Perez"
usuario_edad = 25
usuario_email = "juan@email.com"

# Datos de un producto
producto_nombre = "Laptop"
producto_precio = 999.99
producto_stock = 50

print("✅ Variables de usuario agrupadas:")
print(f"   - {usuario_nombre} {usuario_apellido}, {usuario_edad} años")
print("✅ Variables de producto agrupadas:")
print(f"   - {producto_nombre}, ${producto_precio}, Stock: {producto_stock}")

# ------------------------------------------------
# 10. DOCUMENTAR VARIABLES COMPLEJAS
# ------------------------------------------------
print("\n--- 10. Documentar variables complejas ---")

# ✅ BIEN: Agregar comentarios para variables complejas
# Tasa de conversión de dólares a euros (actualizada: Enero 2026)
TASA_CAMBIO_USD_EUR = 0.92

# Número máximo de conexiones simultáneas permitidas por el servidor
MAX_CONEXIONES = 100

# Tiempo de espera en segundos antes de reintentar una conexión fallida
TIEMPO_REINTENTO = 30

print(f"✅ TASA_CAMBIO_USD_EUR = {TASA_CAMBIO_USD_EUR} (documentada)")
print(f"✅ MAX_CONEXIONES = {MAX_CONEXIONES} (documentada)")
print(f"✅ TIEMPO_REINTENTO = {TIEMPO_REINTENTO} (documentada)")

# ------------------------------------------------
# RESUMEN
# ------------------------------------------------
print("\n" + "="*50)
print("RESUMEN DE BUENAS PRÁCTICAS:")
print("="*50)
print("1. ✅ Usa nombres descriptivos y claros")
print("2. ✅ Usa snake_case (nombre_variable)")
print("3. ✅ Evita palabras reservadas de Python")
print("4. ✅ Inicializa variables con valores apropiados")
print("5. ✅ Usa MAYÚSCULAS para constantes")
print("6. ✅ Sé consistente en el nombramiento")
print("7. ✅ Evita caracteres especiales y números al inicio")
print("8. ✅ Usa tipos de datos apropiados")
print("9. ✅ Agrupa variables relacionadas")
print("10. ✅ Documenta variables complejas")
print("="*50)