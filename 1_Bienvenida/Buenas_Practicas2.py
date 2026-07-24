# ============================================
# BUENAS PRÁCTICAS PARA EL USO DE INPUTS EN PYTHON
# ============================================

print("=== BUENAS PRÁCTICAS DE INPUTS ===\n")

# ------------------------------------------------
# 1. SIEMPRE CONVERTIR EL INPUT AL TIPO DE DATO CORRECTO
# ------------------------------------------------
print("--- 1. Convertir input al tipo correcto ---")

print("❌ MAL: No convertir el input (siempre es string)")
print("Problema: Si no convertimos, no podemos hacer operaciones matemáticas\n")

# Ejemplo INCORRECTO (comentado para que no cause error)
# numero1 = input("Ingresa un número: ")
# numero2 = input("Ingresa otro número: ")
# suma = numero1 + numero2  # Esto concatena strings, no suma números
# print(f"Resultado: {suma}")  # Si ingresa 5 y 3, imprime "53" en lugar de 8

print("✅ BIEN: Convertir al tipo de dato correcto")
print("Usamos int() para enteros, float() para decimales\n")

# Ejemplo CORRECTO con enteros
print("Ejemplo con números enteros:")
numero_entero = int(input("Ingresa un número entero: "))
print(f"Tipo de dato: {type(numero_entero).__name__}")
print(f"Valor ingresado: {numero_entero}")
print(f"Multiplicado por 2: {numero_entero * 2}\n")

# Ejemplo CORRECTO con decimales
print("Ejemplo con números decimales:")
numero_decimal = float(input("Ingresa un número decimal: "))
print(f"Tipo de dato: {type(numero_decimal).__name__}")
print(f"Valor ingresado: {numero_decimal}")
print(f"Dividido por 2: {numero_decimal / 2}\n")

# Ejemplo CORRECTO con texto (no necesita conversión)
print("Ejemplo con texto (string):")
texto = input("Ingresa tu nombre: ")
print(f"Tipo de dato: {type(texto).__name__}")
print(f"Valor ingresado: {texto}")
print(f"En mayúsculas: {texto.upper()}\n")

# ------------------------------------------------
# 2. MANEJO DE ERRORES CON TRY-EXCEPT
# ------------------------------------------------
print("--- 2. Manejo de errores con try-except ---")

print("❌ MAL: Sin manejo de errores")
print("Problema: Si el usuario ingresa texto cuando esperamos un número, el programa falla\n")

# Ejemplo INCORRECTO (comentado para que no cause error)
# edad = int(input("Ingresa tu edad: "))
# print(f"Tu edad es: {edad}")
# Si el usuario ingresa "veinte" en lugar de 20, el programa crashea con ValueError

print("✅ BIEN: Usar try-except para manejar errores")
print("Esto permite que el programa continue si hay un error\n")

# Ejemplo CORRECTO con manejo de errores
print("Ejemplo: Solicitar edad con validación")
while True:
    try:
        edad = int(input("Ingresa tu edad (número entero): "))
        if edad > 0 and edad < 120:
            print(f"✅ Edad válida: {edad} años")
            break
        else:
            print("❌ La edad debe estar entre 1 y 119")
    except ValueError:
        print("❌ Error: Debes ingresar un número entero, no texto")
print()

# Ejemplo CORRECTO con decimales
print("Ejemplo: Solicitar altura con validación")
while True:
    try:
        altura = float(input("Ingresa tu altura en metros (ej: 1.75): "))
        if altura > 0.5 and altura < 2.5:
            print(f"✅ Altura válida: {altura} metros")
            break
        else:
            print("❌ La altura debe estar entre 0.5 y 2.5 metros")
    except ValueError:
        print("❌ Error: Debes ingresar un número decimal válido")
print()

# Ejemplo CORRECTO con validación de texto
print("Ejemplo: Validar respuesta sí/no")
while True:
    respuesta = input("¿Te gusta Python? (s/n): ").lower()
    if respuesta in ['s', 'n']:
        gusta_python = (respuesta == 's')
        print(f"✅ Respuesta válida: {'Sí' if gusta_python else 'No'}")
        break
    else:
        print("❌ Error: Debes responder 's' o 'n'")
print()

# ------------------------------------------------
# 3. USAR MENSAJES CLAROS Y ESPECÍFICOS EN LOS INPUTS
# ------------------------------------------------
print("--- 3. Mensajes claros y específicos ---")

print("❌ MAL: Mensajes vagos o confusos")
print("Problema: El usuario no sabe qué formato o tipo de dato se espera\n")

# Ejemplos INCORRECTOS (comentados)
# dato = input("Dato: ")  # ¿Qué dato?
# num = input("Número: ")  # ¿Entero o decimal? ¿Rango?
# fecha = input("Fecha: ")  # ¿Qué formato? DD/MM/AAAA o MM/DD/AAAA?

print("✅ BIEN: Mensajes claros que indican:")
print("   - Qué dato se espera")
print("   - El formato requerido")
print("   - Ejemplos si es necesario\n")

# Ejemplo CORRECTO: Nombre
print("Ejemplo: Solicitar nombre")
nombre_completo = input("Ingresa tu nombre completo (ej: Juan Pérez): ")
print(f"✅ Nombre ingresado: {nombre_completo}\n")

# Ejemplo CORRECTO: Email con formato
print("Ejemplo: Solicitar email con formato específico")
email = input("Ingresa tu email (ej: usuario@dominio.com): ")
print(f"✅ Email ingresado: {email}\n")

# Ejemplo CORRECTO: Número con rango y tipo
print("Ejemplo: Solicitar calificación con rango")
while True:
    try:
        calificacion = float(input("Ingresa tu calificación (0.0 a 10.0): "))
        if 0.0 <= calificacion <= 10.0:
            print(f"✅ Calificación válida: {calificacion}")
            break
        else:
            print("❌ La calificación debe estar entre 0.0 y 10.0")
    except ValueError:
        print("❌ Error: Ingresa un número decimal válido")
print()

# Ejemplo CORRECTO: Fecha con formato específico
print("Ejemplo: Solicitar fecha con formato explícito")
fecha = input("Ingresa la fecha (formato DD/MM/AAAA, ej: 25/12/2026): ")
print(f"✅ Fecha ingresada: {fecha}")
print("   Nota: En un programa real, validarías el formato con código adicional\n")

# Ejemplo CORRECTO: Selección múltiple con opciones
print("Ejemplo: Selección múltiple con opciones claras")
print("Selecciona tu color favorito:")
print("1. Rojo")
print("2. Azul")
print("3. Verde")
print("4. Amarillo")

while True:
    try:
        opcion = int(input("Ingresa el número de tu opción (1-4): "))
        if 1 <= opcion <= 4:
            colores = ["Rojo", "Azul", "Verde", "Amarillo"]
            print(f"✅ Color seleccionado: {colores[opcion - 1]}")
            break
        else:
            print("❌ Opción inválida, elige entre 1 y 4")
    except ValueError:
        print("❌ Error: Ingresa un número del 1 al 4")
print()

# ------------------------------------------------
# EJEMPLO ADICIONAL: OPERACIONES ARITMÉTICAS CON INPUTS
# ------------------------------------------------
print("="*50)
print("EJEMPLO: CALCULADORA CON INPUTS VALIDADOS")
print("="*50)

print("\nEsta calculadora realiza operaciones con dos números\n")

# Solicitar primer número con validación
while True:
    try:
        num1 = float(input("Ingresa el primer número: "))
        print(f"✅ Primer número: {num1}")
        break
    except ValueError:
        print("❌ Error: Debes ingresar un número válido")

# Solicitar segundo número con validación
while True:
    try:
        num2 = float(input("Ingresa el segundo número: "))
        print(f"✅ Segundo número: {num2}")
        break
    except ValueError:
        print("❌ Error: Debes ingresar un número válido")

# Realizar operaciones aritméticas
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

# Manejar división por cero
if num2 != 0:
    division = num1 / num2
else:
    division = "No se puede dividir por cero"

# División entera y módulo (solo si num2 no es cero)
if num2 != 0:
    division_entera = num1 // num2
    modulo = num1 % num2
else:
    division_entera = "No se puede dividir por cero"
    modulo = "No se puede dividir por cero"

# Potencia
potencia = num1 ** num2

# Mostrar resultados
print("\n" + "="*50)
print("RESULTADOS DE LAS OPERACIONES")
print("="*50)
print(f"Números: {num1} y {num2}")
print(f"Suma (+):           {num1} + {num2} = {suma}")
print(f"Resta (-):          {num1} - {num2} = {resta}")
print(f"Multiplicación (*): {num1} * {num2} = {multiplicacion}")
print(f"División (/):       {num1} / {num2} = {division}")
print(f"División entera (//): {num1} // {num2} = {division_entera}")
print(f"Módulo (%):         {num1} % {num2} = {modulo}")
print(f"Potencia (**):      {num1} ** {num2} = {potencia}")
print("="*50)

# ------------------------------------------------
# EJEMPLO INTEGRADOR: FORMULARIO COMPLETO
# ------------------------------------------------
print("="*50)
print("EJEMPLO INTEGRADOR: FORMULARIO DE USUARIO")
print("="*50)

print("\nPor favor, completa el siguiente formulario:\n")

# Nombre (texto)
nombre = input("1. Ingresa tu nombre: ").strip()
while len(nombre) < 2:
    print("❌ El nombre debe tener al menos 2 caracteres")
    nombre = input("1. Ingresa tu nombre: ").strip()

# Edad (entero con validación)
while True:
    try:
        edad = int(input("2. Ingresa tu edad (18-99 años): "))
        if 18 <= edad <= 99:
            break
        else:
            print("❌ Debes ser mayor de 18 años")
    except ValueError:
        print("❌ Ingresa un número entero válido")

# Altura (decimal con validación)
while True:
    try:
        altura = float(input("3. Ingresa tu altura en metros (1.0-2.5): "))
        if 1.0 <= altura <= 2.5:
            break
        else:
            print("❌ Altura fuera de rango válido")
    except ValueError:
        print("❌ Ingresa un número decimal válido")

# Email (texto con validación básica)
while True:
    email = input("4. Ingresa tu email: ").strip()
    if "@" in email and "." in email:
        break
    else:
        print("❌ Ingresa un email válido (debe contener @ y .)")

# Preferencia (sí/no)
while True:
    preferencia = input("5. ¿Deseas recibir noticias? (s/n): ").lower()
    if preferencia in ['s', 'n']:
        recibir_noticias = (preferencia == 's')
        break
    else:
        print("❌ Responde con 's' o 'n'")

# Mostrar resumen
print("\n" + "="*50)
print("RESUMEN DEL FORMULARIO")
print("="*50)
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Altura: {altura} metros")
print(f"Email: {email}")
print(f"Recibir noticias: {'Sí' if recibir_noticias else 'No'}")
print("="*50)

# ------------------------------------------------
# RESUMEN DE BUENAS PRÁCTICAS
# ------------------------------------------------
print("\n" + "="*50)
print("RESUMEN DE BUENAS PRÁCTICAS PARA INPUTS:")
print("="*50)
print("1. ✅ SIEMPRE convierte el input al tipo correcto")
print("   - Usa int() para enteros")
print("   - Usa float() para decimales")
print("   - No necesitas convertir para texto (string)")
print()
print("2. ✅ SIEMPRE maneja errores con try-except")
print("   - Previene que el programa falle por entradas inválidas")
print("   - Proporciona mensajes de error claros")
print("   - Usa bucles while para reintentar hasta obtener dato válido")
print()
print("3. ✅ SIEMPRE usa mensajes claros y específicos")
print("   - Indica qué tipo de dato se espera")
print("   - Muestra el formato requerido")
print("   - Proporciona ejemplos cuando sea necesario")
print("   - Indica rangos válidos para números")
print("="*50)