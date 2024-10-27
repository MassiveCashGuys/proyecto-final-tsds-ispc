from controllers import controllerUsuario
from validadorDato import ValidacionDatos 


def menu_cambiar_contraseña():
    print("**************************************")
    print("******** Modificar Contraseña ********")
    print("**************************************")
    
    email = solicitar_email()
    usuario = controllerUsuario.recuperar_usuario(email)
    
    if not usuario:
        print("******** El email ingresado es incorrecto ********")
        return
    
    contraseña_actual = solicitar_contraseña_actual(usuario)
    if not contraseña_actual:
        return  
    
    nueva_contraseña = solicitar_nueva_contraseña()
    if nueva_contraseña:
        controllerUsuario.actualizar_contraseña(usuario, nueva_contraseña)
        print("****************************************************")
        print("******** ¡Contraseña cambiada exitosamente! ********")
        print("****************************************************")


def solicitar_email():
    return input("Ingrese el correo con el cual se registró: ")

def solicitar_contraseña_actual(usuario):
    contraseña_actual = input("Ingrese su contraseña actual: ")
    if not ValidacionDatos.verificar_contraseña_actual(usuario, contraseña_actual):
        print("******** La contraseña actual es incorrecta ********")
        return None
    return contraseña_actual

def solicitar_nueva_contraseña():
    nueva_contraseña = input("Ingrese una nueva contraseña: ")
    if ValidacionDatos.pw_es_valido(nueva_contraseña):
        return nueva_contraseña
    else:
        print("La contraseña debe tener entre 8 y 16 caracteres y contener letras, números o símbolos especiales.")
        return None
