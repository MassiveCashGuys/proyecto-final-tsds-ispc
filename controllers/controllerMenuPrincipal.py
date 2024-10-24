from consolaFrontend import menuPrincipal

def menu_principal(inversor):
    if inversor:
      menuPrincipal.mostrar_menu_principal(inversor)
    else:
        print("no existe")