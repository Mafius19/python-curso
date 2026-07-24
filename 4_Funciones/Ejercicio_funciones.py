estado_lampara = "Apagada"

def mostrar_estado():
    print(f"La lampara esta {estado_lampara}")


# global: es un metodo el cual toma la variable global y permite modificarla

def enceder():
    global estado_lampara
    estado_lampara = "encendida"
    print("¡Has encendido la lampara!")

def apagar():
    global estado_lampara
    estado_lampara = "apagada"
    print("¡Has apagado la lampara!")

def menu():
    while True:
        print("---------Menu de la lampara---------")
        print("1- Ver el estado de la lampara")
        print("2- Encender la lampara")
        print("3- Apagar la lampara")
        print("4- Salir")
        opcion = input("Selecciona una opcion: ")
        if opcion == "1":
            mostrar_estado()
        elif opcion == "2":
            enceder()
        elif opcion == "3":
            apagar()
        elif opcion == "4":
            break
        else:
            print("Opcion no valida")

menu()