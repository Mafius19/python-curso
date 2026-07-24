

Lista = ["A","C","F","B"] #Lista de datos

"""
["Manzana","Banana","Melon","Manzana",1]
[    0    ,   1    ,   2   ,    3    ,4]
"""
#Vemos la longitud de la lista
print (len(Lista))

#Añadimos un elemento a la lista
Lista.append("Uva")
#Insertamos un elemento en un espacio especifico
Lista.insert(2,"Mandarina")
print(Lista)
#Removemos un elemento de la lista
Lista.remove("A")
print(Lista)
#Removemos el ultimo elemento de la lista
Lista.pop()
print(Lista)
#Removemos un elemento de la lista por su indice
del Lista[1]
print(Lista)

#Ordenamos la lista
Lista.sort()
#Ordenamos la lista de forma inversa
Lista.reverse()
print(Lista)
