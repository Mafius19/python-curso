#tupla declaración normal

mi_tupla = (1,2,3,4,5) #Una tupla no se puede modificar

#tupla de un solo valor 

tupla_unValor = (1,)

print(f"Esta es mi primer tupla {mi_tupla}")
print(f"Esta es mi tupla de un solo valor {tupla_unValor}")

#Tupla solo con comas (sin parentesis)

tupla_comas = 1,2,3,4,5,"kevin","Walter"

print(f"Esta es mi tupla con comas {tupla_comas}")
#Tupla con cosntructor tuple
tupla_nueva = tuple()
tupla_desdeBD = tuple([1,2,3])

print(tupla_nueva)
print(tupla_desdeBD)

#Ejemplo:

coordenadas = (40.7128, -74.0060,"Nueva York")

print(coordenadas)

print("Coordenadas 1: ",coordenadas[0])
print("Coordenadas 2: ",coordenadas[1])
print("Coordenadas 3: ",coordenadas[2])

latitud,longitud,ciudad = coordenadas

print(f"Ciudad: {ciudad}, Latitud: {latitud}, Longitud: {longitud}")


estudiantes = {
        "Ana": 8.5,
        "Luis": 6.0,
        "Pedro": 4.8,
        "Lucía": 7.2,
        "Carlos": 5.5,
        "María": 9.1
    }

for estudiante in estudiantes:
  print(estudiante)
  print(estudiantes[estudiante])
  