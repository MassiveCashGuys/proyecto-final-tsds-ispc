from controllers import controllerMenuPrincipal, controllerRegistrarInversor, controllerInicioSesion, controllerUsuario
from negocio import usuario, servicioReglasNegocio
from backend.clasesDAO.usuario_dao import Usuario_Dao
from consolaFrontend import menu_recuperar_password
import getpass
import os

def recuperar_contraseña():
    contraseña=""
    return contraseña

def menu_inicio_sesion():
    print(f"*******INICIO SESIÓN/ REGISTRO*******")
    print(f"1. Ingresar Usuario y Contraseña")
    print(f"2. Nuevo Usuario.")
    print(f"3. Recuperar mi Contraseña.")
    print(f"4. Modificar mi Contraseña ")
    print(f'5- salir del sistema.')
    
def mostar_menu_inicio_sesion():
     while True:
        menu_inicio_sesion()
        opcion = int(input(f"Seleccione una opción (1-5): "))

        if opcion == 1: # Gus
            user = menu_inicio_login()

            """   Seguir con la validación de la contraseña despues!!!     
            aux = controllerInicioSesion.obtener_usuario(user.get_id_user())
            print(user)
            print(aux)
            validar_ingreso(aux, user.get_password())
            """

        elif opcion == 2:
            print(f"Nuevo Usuario.")
            controllerRegistrarInversor.cargar_menu_registro_inversor()
        elif opcion == 3:
            menu_recuperar_password.menu_recuperar_contraseña()
             
        elif opcion == 4:
            print(f"Modificar mi contraseña.")
        elif opcion == 5:
            print(f"Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 5.")


# Gustavo 
# Tarea 14 y 16
def menu_inicio_login():
    print("\n")
    print(f"******************************")
    print(f"**     INICIO DE SESIÓN     **")
    print(f"******************************")
    print("\n")
    email = input(f'Ingrese su correo: ')
    password = input(f'Ingrese su contraseña: ')



    # Verifica si el email existe en la base de datos
    usuario_dao = Usuario_Dao()
    user = usuario_dao.get(email)

    if user:        

        # Verifica si la contraseña es correcta
        if servicioReglasNegocio.validar_password(password, user.get_password()):
            print("\n")
            print(" ✅ Ingreso correcto ✅")
            print("\n")
            print("Bienvenido " + user.get_id_user() + " 🙋‍♂️ 🙋‍♀️") # Cambiar para que agregue el nombre desde inventario.
            print("\n")            
            return user
        else:
            print("\n")
            print("Error: Email o Contraseña incorrecta ⚠️ ")
            print("\n")
            return None
    else:
        print("\n")
        print("Error: Email o Contraseña incorrecta ⚠️ ")
        print("\n")
        return None
    
    
    

# Seguir con la validación de la contraseña despues!!!
"""
def validar_ingreso(user, password):
    #if user:
        print(controllerInicioSesion.validar_password(user, password))

        if controllerInicioSesion.validar_password(user, password):
            print("Ingreso correcto")
        else:
            print("Ingreso incorrecto")
    else:  
        print("Ingreso incorrecto")
"""


