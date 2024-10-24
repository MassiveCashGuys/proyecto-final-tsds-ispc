
from consolaFrontend import menu_lista_acciones
from controllers import controllerAccion, controllerTransaccion
from negocio import transaccion, servicioReglasNegocio, tipoTransaccion


def mostrar_menu_comprar_acciones(inversor):
    accion = menu_lista_acciones.menu_accion()
    cantidad_comprada = int(input(f'Ingrese la cantidad de acciones que desea comprar:'))
    accion.set_cantidad(accion.get_cantidad() -cantidad_comprada)
    print (accion.get_cantidad())
    nueva_transaccion = transaccion.Transaccion(
        None, 
        servicioReglasNegocio.definir_fecha_actual(servicioReglasNegocio.formato_fecha_hora()),
        cantidad_comprada, 
        accion.get_precio_venta_actual(),
        servicioReglasNegocio.calcular_comision_broker(accion.get_precio_venta_actual()*cantidad_comprada), 
        inversor.get_cuit(), 
        accion.get_id_accion(), 
        tipoTransaccion.TipoTransaccion(1,None,None))
    controllerTransaccion.crear_transaccion(nueva_transaccion)
    controllerAccion.actualizar_accion(accion)
    
    
    
    
    