def menu_tipo_documento(titulo, moduloController):
    print(f"*******{titulo}*******")
    lista_tipo =  moduloController.obtener_lista_tipo()
   
    for doc in lista_tipo :
        print(f'{doc.get_nombre()} - {doc.get_descripcion()} ')
    return lista_tipo


def mostar_menu_tipo(textoIngreso):
        lista = menu_tipo_documento()
        opcion = input(f'Ingrese un tipo de {textoIngreso}: ')
        return obtener_tipo(opcion,lista)
       

def obtener_tipo (opcion, lista):
    for tipo in lista:
        if tipo.get_nombre() == opcion.upper():
            return tipo
    return None