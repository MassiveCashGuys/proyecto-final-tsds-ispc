from controllers import controllerTipoDocumento
from negocio import tipoDocumento
def menu_tipo_documento():
    print(f"*******Tipo de Documentos*******")
    lista_tipo_documento = controllerTipoDocumento.obtener_lista_tipo_documento()
   
    for doc in lista_tipo_documento :
        print(f'{doc.get_nombre()} - {doc.get_descripcion()} ')
    return lista_tipo_documento


def mostar_menu_tipo_documento():
        lista = menu_tipo_documento()
        opcion = input(f'Ingrese un tipo de documento solo las iniciales')
        print(obtener_tipo_documento(opcion,lista).get_descripcion())
       

def obtener_tipo_documento (opcion, lista)->tipoDocumento.TipoDocumento:
    for doc in lista:
        if doc.get_nombre() == opcion.upper():
            return doc
    return None