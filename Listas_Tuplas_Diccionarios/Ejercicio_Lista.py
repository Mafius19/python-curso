lista_compra =[]

while True:
    
    print("\n----- Lista Super Mercado")
    print("1- Agregar producto")
    print("Ver lista de compras")
    print("3- Eliminar producto")
    print("4- Cantidad de productos")
    print("5- Salir del menu")

    opcion = input("\nSelecciona una opción del menu")

    if opcion == "5":
        print("\nGracias por usar la lista de compras")
        break

    
    elif opcion == "1":
        print("\nOpción seleccionada: Agregar producto")
        producto = input("Ingresa el nombre del producto: ")
        if producto:
            lista_compra.append(producto)
            print(f"Producto: {producto} ha sido añadido exitosamente.")
        else:
            print("No se puede agregar un producto vacio, añadelo nuevamente")
    elif opcion == "2":
        print("\nOpción seleccionada: Ver lista de compras")
        print("-----Lista de compras---------")
        if not lista_compra:
            print("La lista de compras esta vacia")
        else:
            for i, producto in enumerate(lista_compra,1):
                print(f"{i}- {producto}")
    elif opcion == "3":
        print("\nOpción seleccionada: Eliminar producto")
        print("---Eliminar un prodcuto de la lista")
        if not lista_compra:
            print("La lista de compras esta vacia")
        else:
            print("Lista actual de productos: ")
            for i, producto in enumerate(lista_compra,1):
                print(f"{i}- {producto}")

            try:
                num_product= int(input("Ingresa el numero del producto a eliminar: "))
                if 1<= num_product <= len(lista_compra):
                    producto_elimando = lista_compra.pop(num_product - 1)
                    print(f"El producto {producto_elimando} ha sido eliminado exitosamente.")
                else:
                    print("El numero ingresado no es valido")
            except ValueError:
                print("Por favor ingresa un numero valido ")
    elif opcion == "4":
        print("\nOpción seleccionada: Ver cantidad de productos")
        print("-------Cantidad de productos---------")
        if not lista_compra:
            print("Lista vacia")
        else:
            cantidad = len(lista_compra)
            if cantidad == 1:
                print(f"Tienes un producto en la lista")
            else:
                print(f"Tienes {cantidad} productos en la lista")
    else:
        print("\nOpción no válida. Por favor, selecciona una opción del 1 al 5.")
