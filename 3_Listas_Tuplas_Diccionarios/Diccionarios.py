#tupla declaracion normal

mi_tupla = (1,2,3,4,5) #Una tupla no se puede modificar

#tupla de un solo valor

tupla_unValor = (1,)

print(f"Esta es mi primer tupla {mi_tupla}")
print(f"Esta es mi tupla de un solo valor {tupla_unValor}")

#tuplas solo con comas (sin parentesis)

tuplas_comas = 1,2,3,4,5,"kevin","Walter"

print(f"Esta es mi tupla con comas {tuplas_comas}")

#tupla con constructor tuple

tupla_nueva = tuple()
tupla_constructor = tuple([1,2,3,4,5])

print(tupla_nueva)
print(f"Esta es mi tupla con constructor {tupla_constructor}")

#Ejemplo

coordenadas = (40.7128, -74.0060, "Nueva York")
print(f"Coordenadas: {coordenadas}")

print("Coordenandas 1:", coordenadas[0])
print("Coordenandas 2:", coordenadas[1])
print("Coordenandas 3:", coordenadas[2])

latitud, longitud, ciudad = coordenadas

print(f"Ciudad: {ciudad}, Latitud: {latitud}, Longitud: {longitud}")