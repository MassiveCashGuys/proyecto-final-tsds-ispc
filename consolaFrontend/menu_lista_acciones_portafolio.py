# from controllers import controllerAccion
from controllers import controllerDetallePortafolio
from negocio import detallePortafolio


# def menu_accion_portafolio(inversor) -> accion.Accion:
def menu_accion_portafolio(inversor) -> detallePortafolio.DetallePortafolio:

    id_portafolio_user = (inversor.get_portafolio().get_id_portafolio())
   
    lista_acciones_portafolio = controllerDetallePortafolio.obtener_acciones_portafolio(
        id_portafolio_user)
    
    for detalle in lista_acciones_portafolio:
        print(
            f'Simbolo: {detalle.get_accion_id_accion().get_simbolo()} - Acción: {detalle.get_accion_id_accion().get_nombre()} - Precio de venta actual ${detalle.get_accion_id_accion().get_precio_venta_actual()} - Cantidad Compradas: {detalle.get_cantidad_acciones_compradas()}')
    opcion = input(f'Ingrese el simbolo de la accion que desea vender:')
    accion = obtener_simbolo(opcion, lista_acciones_portafolio)
    return accion


def obtener_simbolo(opcion, lista):
    for accion in lista:
        if accion.get_accion_id_accion().get_simbolo() == opcion.upper():
            return accion
    return None
