def alcancilla(moneda):
    if moneda == 0:
        print("La alcancilla esta vacia")
        return 0
    else:
        print("Has sacado una moneda de tu alcancia quedan :",moneda - 1)
        return 1 + alcancilla(moneda -1)


alcancilla(5)