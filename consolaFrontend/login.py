from controllers import controllerMenuPrincipal, controllerRegistrarInversor


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

        if opcion == 1:
            print(f"Ingresar Usuario y Contraseña")
            controllerMenuPrincipal.menu_principal()
        elif opcion == 2:
            print(f"Nuevo Usuario.")
            controllerRegistrarInversor.cargar_menu_tipo_documento()
        elif opcion == 3:
            print(f"Recuperar mi Contraseña.")
        elif opcion == 4:
            print(f"Recuperar mi Usuario.")
        elif opcion == 5:
            print(f"Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 5.")