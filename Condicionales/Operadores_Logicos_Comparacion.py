nombre = "Carlos" #Al utilizar un signo de = es asignar valor
edad = 15
rango_Edad = 18

#Operadores de comparacion
if nombre  == "Kevin" : #utilizar dos signos == es comparar valor  si es igual el resultado es TRUE
    print ("Bienvenido : ", nombre)


if nombre != "Kevin": # El resultado del if es TRUE si el valor de la izquierda es diferente al de  la derecha
    # Nombre(variable) = Carlos  nombre != Kevin
    print("Tu no eres Kevin")

if(edad > rango_Edad): #El valor de edad es mayor al rango  de edad el resultadoes TRUE
    print("Tu eres mayor de edad")

if(edad < rango_Edad): #El valor de edad es menor al rango  de edad el resultadoes TRUE
    print("Tu eres menor de edad")

if edad >= 15: # Si el valor de la izquierda es mayor o igual al  valor de la derecha, el  resultado es TRUE
    print("Tu edad es de 15 años");

if edad <= 15: # Si el valor de la izquierda es menor o igual al  valor de la derecha, el  resultado es TRUE
    print("Tu edad es de 15 años");


    #Operadores Logicos

#AND: es un operador que evalua si dos condiciones son verdaderas

Numero1 = 10;
Numero2 = 10;
Numero3 = 10;
if Numero1 == 10 and Numero2 == 10: #and = y, si la  primera condicion  y la segunda  son correctos el resultado es true
    print ("Los dos numeros son igual a 10")

#OR: es un operador que evalua si una de las condiciones es verdadera se  ejecutara igualmente
if Numero1  == Numero2 or Numero1 != Numero3 :  # La primera condicional es verdadera entonces el resultado es TRUE
    # or = o si  un valor es igual a otro "o(OR)" este otro valor es diferente a otro  entonces sera true
    print ("Una de las sentencias se  ha cumplido")

#NOT: El  operador NOT invierte los resultados  dependiendo de su valor (TRUE O FALSE)

Licencia = True #con el operador not Licencia = False
Edad = 15;

if Edad == 18 or not Licencia == False:

        print ("Tu edad no es suficiente para tener licencia")