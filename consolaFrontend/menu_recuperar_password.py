from controllers import controllerUsuario
from service import servicioEmail

def menu_recuperar_contraseña():
    print(f"********Recuperar Contraseña********")
    email = input(f'Ingrese el correo con cual se registro: ')
    usuario_recuperado = controllerUsuario.recuperar_password(email)
    if  usuario_recuperado :
       servicioEmail.crear_mensaje(usuario_recuperado)
      
    else:
        print(f'El email ingresado es incorrecto')

