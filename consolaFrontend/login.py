from controllers import controllerMenuPrincipal, controllerRegistrarInversor, controllerInicioSesion
from negocio import usuario
from backend.clasesDAO.usuario_dao import Usuario_Dao
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
    print(f"4. Recuperar mi Usuario")
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
            print(f"Recuperar mi Contraseña.")
        elif opcion == 4:
            print(f"Recuperar mi Usuario.")
        elif opcion == 5:
            print(f"Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 5.")


# Gustavo 
"""
def menu_ingreso():
    print(f"*******INICIO SESIÓN*******")
    email = input(f'Ingrese su correo: ')
    password = input(f'Ingrese su contraseña: ')
    user = usuario.Usuario(email, password, None)
    
# Verifica si los datos existen en la base de datos
    user = controllerInicioSesion.obtener_usuario(email)
    
    if user:
        # Verifica si la contraseña es correcta
        if controllerInicioSesion.validar_password(user, password):
            print("Ingreso correcto")
            return user
        else:
            print("Contraseña incorrecta")
            return None
    else:
        print("Correo electrónico no encontrado")
        return None
    """
def menu_inicio_login():
    print("\n")
    print(f"*******INICIO DE SESIÓN*******")
    print("\n")
    email = input(f'Ingrese su correo: ')
    
    # Verifica si el email existe en la base de datos
    usuario_dao = Usuario_Dao()
    user = usuario_dao.get(email)

    if user:

        password = input(f'Ingrese su contraseña: ')

        # Verifica si la contraseña es correcta
        if user.get_password() == password:
            print("\n")
            print(" ✅ Ingreso correcto ✅")
            print("\n")
            print("Bienvenido " + user.get_id_user() + " 🙋‍♂️ 🙋‍♀️")
            print("\n")
            print("Datos del usuario: " + user.__str__())
            print("\n")
            return user
        else:
            print("\n")
            print(" ⚠️ Contraseña incorrecta ⚠️ ")
            print("\n")
            return None
    else:
        print("\n")
        print(" ⚠️ Correo electrónico no encontrado ⚠️ ")
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


