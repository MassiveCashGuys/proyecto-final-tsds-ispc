from controllers import controllerMenuPrincipal

def recuperar_contraseña():
    contraseña=""
    return contraseña


def menu_inicio_sesion():
    print(f"*******LOGIN*******")
    print(f"1. Ingresar Usuario y Contraseña")
    print(f"2. Recuperar mi Contraseña.")
    print(f"3. Recuperar mi Usuario")
    print(f'4- Cerrar sesión y salir del sistema.')
    
def mostar_menu_inicio_sesion():
     while True:
        menu_inicio_sesion()
        opcion = int(input("Seleccione una opción (1-4): "))

        if opcion == 1:
            print("Ingresar Usuario y Contraseña")
            controllerMenuPrincipal.menu_principal()
        elif opcion == 2:
            print("Recuperar mi Contraseña.")
        elif opcion == 3:
            print("Recuperar mi Usuario.")
        elif opcion == 4:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 4.")