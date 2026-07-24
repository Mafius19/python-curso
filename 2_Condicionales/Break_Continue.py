
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
       continue
    print(contador)

print("El bucle ha terminado")

# Ejemplo de break y continue
print("Ejemplo de break:")
for i in range(1, 11):
    if i == 5:
        print("¡Se encontró el 5! Terminando el bucle...")
        break  # Sale completamente del bucle
    print(f"Número: {i}")

    print("\nEjemplo de continue:")
for i in range(1, 11):
    if i % 2 == 0:  # Si el número es par
        continue  # Salta a la siguiente iteración sin ejecutar el resto del código
    print(f"Número impar: {i}")

# Ejemplo combinado
print("\nEjemplo combinado (números del 1 al 10, parar en 7):")
for i in range(1, 11):
    if i > 7:
        break  # Sale del bucle cuando i es mayor que 7
    if i % 2 == 0:
        continue  # Salta los números pares
    print(f"Número impar menor o igual a 7: {i}")
