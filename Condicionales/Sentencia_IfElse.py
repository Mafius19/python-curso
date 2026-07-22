# Sentencia If-Else y IF

Edad = int(input("Ingrese su edad: "))

if Edad  < 18:
    print("Aún no puedes votar. Debes tener al menos 18 años.")
else:
    print("¡Puedes votar en las próximas elecciones!")


print("Fin del programa")

edad = int(input("Ingrese su edad: "))

# Sentencia If-Elif-Else

if edad < 13:
    print("Eres menor de edad")
elif edad >= 13 and edad < 18:
    print("Eres adolescente")
elif edad >= 18 and edad < 60:
    print("Eres adulto")
else:
    print("Eres adulto mayor")