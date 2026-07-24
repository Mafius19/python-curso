"""
Programa para calcular el promedio final de un estudiante a partir de 3 notas
y mostrar si aprueba o reprueba (nota mínima para aprobar: 6.0).
"""

# Constantes
NOTA_MINIMA = 6.0
NOTA_MIN = 0.0
NOTA_MAX = 10.0
NUMERO_NOTAS = 3

def calcular_promedio(*notas):
    """
    Calcula el promedio de una lista de notas.
    
    Args:
        *notas: Una o más notas numéricas
        
    Returns:
        float: El promedio de las notas
    """
    return sum(notas) / len(notas)

def evaluar_aprobacion(promedio, nota_minima=NOTA_MINIMA):
    """
    Evalúa si un estudiante aprueba según su promedio.
    
    Args:
        promedio (float): El promedio del estudiante
        nota_minima (float, optional): Nota mínima para aprobar. 
                                     Por defecto es NOTA_MINIMA.
        
    Returns:
        str: "Aprobado" o "Reprobado"
    """
    return "Aprobado" if promedio >= nota_minima else "Reprobado"

def obtener_nota(mensaje):
    """
    Solicita una nota al usuario con validación.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        
    Returns:
        float: Nota válida ingresada por el usuario
    """
    while True:
        try:
            nota = float(input(mensaje))
            if NOTA_MIN <= nota <= NOTA_MAX:
                return nota
            print(f"Error: La nota debe estar entre {NOTA_MIN} y {NOTA_MAX}")
        except ValueError:
            print("Error: Por favor ingrese un número válido")

def main():
    """Función principal del programa."""
    print("\n" + "="*50)
    print("        CALCULADORA DE NOTAS FINALES")
    print("="*50)
    
    # Obtener notas del usuario
    notas = []
    for i in range(1, NUMERO_NOTAS + 1):
        nota = obtener_nota(f"Ingresa la nota {i} (entre {NOTA_MIN} y {NOTA_MAX}): ")
        notas.append(nota)
    
    # Calcular promedio y evaluar aprobación
    promedio = calcular_promedio(*notas)
    estado = evaluar_aprobacion(promedio)
    
    # Mostrar resultados
    print("\n" + "-"*50)
    print("RESULTADOS:")
    print("-"*50)
    
    for i, nota in enumerate(notas, 1):
        print(f"Nota {i}: {nota:5.2f}")
    
    print("-"*50)
    print(f"Promedio: {promedio:5.2f}")
    print(f"Estado:   {estado}")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()