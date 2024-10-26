from consolaFrontend.menu_inicio_sesion import menu_inicio_login
from controllers import controllerInversor, controllerMenuPrincipal, controllerRegistrarInversor, controllerInicioSesion, controllerUsuario
from negocio import usuario, servicioReglasNegocio
from backend.clasesDAO.usuario_dao import Usuario_Dao
from consolaFrontend import menu_recuperar_password

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
            if user:
               controllerMenuPrincipal.menu_principal(controllerInversor.obtener_inversor(user))
            
        elif opcion == 2:
            print(f"Nuevo Usuario.")
            inversor = controllerRegistrarInversor.cargar_menu_registro_inversor()
            controllerMenuPrincipal.menu_principal(inversor)
            break
        
        elif opcion == 3:
            menu_recuperar_password.menu_recuperar_contraseña()
             
        elif opcion == 4:
            print(f"Modificar mi contraseña.")
        elif opcion == 5:
            print(f"Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 5.")



    
    




