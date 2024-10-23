def menu_tipo(titulo, moduloController):
    print(f"*******{titulo}*******")
    lista_tipo =  moduloController.obtener_lista_tipo()
    i=1
    for doc in lista_tipo :
        print(f'{i} - {doc.get_nombre()}')
        i+=1
    return lista_tipo
""" - {doc.get_descripcion()}  """

def mostar_menu_tipo(titulo, moduloController, ingresoDato):
        lista = menu_tipo(titulo, moduloController)
        opcion = input(f'Ingrese un tipo de {ingresoDato}: ')
        return obtener_tipo(opcion,lista)
       

def obtener_tipo (opcion, lista):
    for tipo in lista:
        if tipo.get_nombre() == opcion.upper():
            return tipo
    return None