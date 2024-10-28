from controllers import controllerUsuario
from validadorDato import ValidacionDatos



def menu_cambiar_contraseña():

    mostrar_titulo("Modificar Contraseña")
    email = input("Ingrese el correo con el cual se registró: ")
    usuario_recuperado = controllerUsuario.recuperar_usuario(email)
    
    if usuario_recuperado:
        contraseña_actual = input("Ingrese su contraseña actual: ")
        
        if controllerUsuario.verificar_contraseña_actual(usuario_recuperado, contraseña_actual):
            print("Contraseña actual verificada. La nueva contraseña debe tener entre 8 y 16 caracteres y contener letras, números o símbolos especiales.")
            
            while True:
                nueva_contraseña = input("Contraseña: ")
                if ValidacionDatos.pw_es_valido(nueva_contraseña):
                    break
                else:
                    print("La contraseña debe tener entre 8 y 16 caracteres y contener letras, números o símbolos especiales.")
            
            controllerUsuario.modificar_pasword(usuario_recuperado,nueva_contraseña)

            mostrar_titulo("¡Contraseña Modificada!")

        else:
            print("**La contraseña actual es incorrecta**")
            
    else:
        print("**El email ingresado es incorrecto**")


def mostrar_titulo(titulo):
    print(" ")
    print("*************************************")
    print(f'         {titulo}                ')
    print("*************************************")
    print(" ")