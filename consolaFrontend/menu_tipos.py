def menu_tipo(titulo, moduloController):
    print(f"*******{titulo}*******")
    lista_tipo =  moduloController.obtener_lista_tipo()
   
    for doc in lista_tipo :
        print(f'{doc.get_nombre()} - {doc.get_descripcion()} ')
    return lista_tipo


def mostar_menu_tipo(titulo, moduloController, ingresoDato):
        lista = menu_tipo(titulo, moduloController)
        opcion = input(f'Ingrese un tipo de {ingresoDato}: ')
        return obtener_tipo(opcion,lista)
       

def obtener_tipo (opcion, lista):
    for tipo in lista:
        if tipo.get_nombre() == opcion.upper():
            return tipo
    return None