from controllers import controllerRegistrarInversor, controllerPortafolio
def menu_principal():
    print(f'****************ARGBROKER****************')
    print(f'1- Comprar Acciones.')
    print(f'2- Vender Acciones.')
    print(f'3- Ver Saldo.')
    print(f'4- Opción.')
    print(f'5- Opción.')
    print(f'6- Cerrar sesión y salir del sistema.')
    

def mostrar_menu_principal(inversor):
    while True:
        menu_principal()
        opcion = int(input(f"Seleccione una opción (1-6): "))
        
        if opcion == 1:
            print(f"Opción 1")
            
            input("Presiona cualquier tecla para continuar...")
        elif opcion == 2:
            print(f" Opción 2-en progreso de codificacion...")
            input("  Presiona cualquier tecla para continuar...")
        elif opcion == 3:
            print(f"***** Saldo *****")
            print(f'${controllerPortafolio.obteder_portafolio(inversor.get_portafolio()).get_saldo_actual()}')
            input("Presiona cualquier tecla para continuar...")
        elif opcion == 4:
            print(f"  Opción 4 - en progreso de codificacion...")
            input("  Presiona cualquier tecla para continuar...")
            break
        elif opcion == 5:
            print(f" Opción 5 - en progreso de codificacion...")
            input("  Presiona cualquier tecla para continuar...")
            break
        elif opcion == 6:
            print(f"Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 6.")