numero = int(input("Ingresa un numero entero porfavor"))

while numero < 0:

    print("¡Error el numero debe ser positivo!")
    numero = int(input("Ingresa un numero entero porfavor"))

print("Cuenta regresiva")
while  numero >= 0:
    print(numero)
    numero -= 1

#Ejercicio for

texto = input("Ingresa una palabra o frase: ")

contador = 0

for letra in texto:
    
    if letra.lower() in "aeiouáéíóúü":
        contador += 1
    
print(f"La palabra o frase {texto} tiene {contador} vocales")