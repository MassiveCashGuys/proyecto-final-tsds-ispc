def menu_principal():
    print(f'****************ARGBROKER****************')
    print(f'1- Opción.')
    print(f'2- Opción.')
    print(f'3- Opción.')
    print(f'4- Opción.')
    print(f'5- Opción.')
    print(f'6- Cerrar sesión y salir del sistema.')
    

def mostrar_menu_principal():
    while True:
        menu_principal()
        opcion = int(input(f"Seleccione una opción (1-6): "))

        if opcion == 1:
            print(f" Opción 1")
        elif opcion == 2:
            print(f" Opción 2.")
        elif opcion == 3:
            print(f" Opción 3")
        elif opcion == 4:
            print(f" Opción 4.")
            break
        elif opcion == 5:
            print(f" Opción 5.")
            break
        elif opcion == 6:
            print(f"Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 6.")