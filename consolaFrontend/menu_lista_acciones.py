from controllers import controllerAccion
from negocio import accion


def menu_accion() -> accion.Accion:
    lista_acciones = controllerAccion.obtener_acciones()

    for accion in lista_acciones:
        print(f'Simbolo: {accion.get_simbolo()} - Acción: {accion.get_nombre()} - Unidad ${accion.get_precio_venta_actual()} - Disponibles: {accion.get_cantidad()}')
    opcion = input(f'Ingrese el simbolo de la accion que desea comprar:')
    accion = obtener_simbolo(opcion, lista_acciones)
    return accion


def obtener_simbolo(opcion, lista):
    for accion in lista:
        if accion.get_simbolo() == opcion.upper():
            return accion
    return None
