from controllers import controllerUsuario
import validadorDato.ValidacionDatos
from negocio import servicioReglasNegocio



def menu_cambiar_contraseña():
    print("********Cambiar Contraseña********")
    
    email = input("Ingrese el correo con el cual se registró: ")
    usuario_recuperado = controllerUsuario.recuperar_usuario(email)
    
    if usuario_recuperado:
        contraseña_actual = input("Ingrese su contraseña actual: ")
        
        if controllerUsuario.verificar_contraseña_actual(usuario_recuperado["usuario"], contraseña_actual):
            print("Contraseña actual verificada. Ahora puede ingresar una nueva contraseña.")
            
            nueva_contraseña = input("Ingrese una nueva contraseña: ")
            
            contraseña_encriptada = servicioReglasNegocio.crear_encriptacion_password(nueva_contraseña)
            controllerUsuario.actualizar_contraseña(usuario_recuperado["usuario"], contraseña_encriptada)
            
            print("¡Contraseña cambiada exitosamente!")
        else:
            print("La contraseña actual es incorrecta.")
    else:
        print("El email ingresado es incorrecto.")
