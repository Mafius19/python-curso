
def validacion(request,data):
    correcto = request
    userdata = data

    return correcto,userdata



request,dataUser = validacion(True,'Coto')

print(request,dataUser)