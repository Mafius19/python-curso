

def data_user(user):

    def validacion(user_data):
       

        return user_data == "admin"
    
    if validacion(user):
        print("Acceso concedido")
    else: 
        print("Acceso denegado")
    
    return user

acceso = data_user("pollito")

print(f"El acceso del usuario: {acceso}")