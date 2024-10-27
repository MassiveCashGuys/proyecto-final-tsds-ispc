# from consolaFrontend import menu_lista_acciones
from consolaFrontend import menu_lista_acciones_portafolio
from controllers import controllerAccion, controllerDetallePortafolio, controllerPortafolio, controllerTransaccion
from negocio import detallePortafolio, portafolio, transaccion, servicioReglasNegocio, tipoTransaccion, accion


def verificar_acciones_disponibles(cantidad_acciones_disponibles, cantidad_a_vender):
    return cantidad_acciones_disponibles >= cantidad_a_vender


def mostrar_menu_vender_acciones(inversor):
    accion_portafolio = menu_lista_acciones_portafolio.menu_accion_portafolio(
        inversor)

    cantidad_acciones_disponibles = accion_portafolio.get_cantidad_acciones_compradas()

    while True:
        cantidad_a_vender = int(
            input(f'Ingrese la cantidad de acciones que desea vender: '))
        if verificar_acciones_disponibles(cantidad_acciones_disponibles, cantidad_a_vender):
            accion_portafolio.get_accion_id_accion().set_cantidad(
                accion_portafolio.get_accion_id_accion().get_cantidad() + cantidad_a_vender)
            print(accion_portafolio.get_accion_id_accion().get_cantidad())
                 
          
            nueva_transaccion = transaccion.Transaccion(
                None,
                servicioReglasNegocio.definir_fecha_actual(
                    servicioReglasNegocio.formato_fecha_hora()),
                cantidad_a_vender,
                accion_portafolio.get_accion_id_accion().get_precio_venta_actual(),
                servicioReglasNegocio.calcular_comision_broker(
                    accion_portafolio.get_accion_id_accion().get_precio_venta_actual()*cantidad_a_vender),
                inversor.get_cuit(),
                accion_portafolio.get_accion_id_accion().get_id_accion(),
                tipoTransaccion.TipoTransaccion(2, None, None))
            transaccion_creada = controllerTransaccion.crear_transaccion(
                nueva_transaccion)
            
            inversor.get_portafolio().set_saldo_actual(( (cantidad_a_vender * accion_portafolio.get_accion_id_accion().get_precio_venta_actual()) -(servicioReglasNegocio.calcular_comision_broker(cantidad_a_vender*accion_portafolio.get_accion_id_accion().get_precio_venta_actual())) + inversor.get_portafolio().get_saldo_actual()))
                        
             
            controllerPortafolio.actualizar_saldo_portafolio(inversor.get_portafolio())
            

            break
        else:
            print(
                f"Acciones insuficientes. Su cantidad de acciones disponible es {cantidad_acciones_disponibles} y el total que queres vender es {cantidad_a_vender}.")
            print("Por favor, ingrese una cantidad menor de acciones.")
    