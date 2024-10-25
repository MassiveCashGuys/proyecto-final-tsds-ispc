
from consolaFrontend import menu_lista_acciones
from controllers import controllerAccion, controllerDetallePortafolio, controllerPortafolio, controllerTransaccion
from negocio import detallePortafolio, portafolio, transaccion, servicioReglasNegocio, tipoTransaccion


def verificar_saldo(saldo_actual_portafolio, total_del_valor_compra):
    return saldo_actual_portafolio >= total_del_valor_compra


def mostrar_menu_comprar_acciones(inversor):
    accion = menu_lista_acciones.menu_accion()
    portafolio_del_inversor = controllerPortafolio.obteder_portafolio(
        inversor.get_portafolio())

    saldo_actual_portafolio = portafolio_del_inversor.get_saldo_actual()

    while True:
        cantidad_comprada = int(
            input(f'Ingrese la cantidad de acciones que desea comprar: '))
        total_del_valor_compra = accion.get_precio_venta_actual() * cantidad_comprada

        if verificar_saldo(saldo_actual_portafolio, total_del_valor_compra):
            break
        else:
            print(
                f"Saldo insuficiente. Su saldo es {saldo_actual_portafolio} y el total de la compra es {total_del_valor_compra}.")
            print("Por favor, ingrese una cantidad menor de acciones.")

    accion.set_cantidad(accion.get_cantidad() - cantidad_comprada)
    print(accion.get_cantidad())
    nueva_transaccion = transaccion.Transaccion(
        None,
        servicioReglasNegocio.definir_fecha_actual(
            servicioReglasNegocio.formato_fecha_hora()),
        cantidad_comprada,
        accion.get_precio_venta_actual(),
        servicioReglasNegocio.calcular_comision_broker(
            accion.get_precio_venta_actual()*cantidad_comprada),
        inversor.get_cuit(),
        accion.get_id_accion(),
        tipoTransaccion.TipoTransaccion(1, None, None))
    transaccion_creada = controllerTransaccion.crear_transaccion(
        nueva_transaccion)
    controllerAccion.actualizar_accion(accion)
    portafolio_actual = controllerPortafolio.obteder_portafolio(
        inversor.get_portafolio())
    portafolio_actual.set_saldo_actual(portafolio_actual.get_saldo_actual(
    ) - (accion.get_precio_venta_actual()*cantidad_comprada) - transaccion_creada.get_comision_broker())
    print(portafolio_actual.get_saldo_actual())
    controllerPortafolio.actualizar_saldo_portafolio(portafolio_actual)
    """ nuevoDetallePortafolio=portafolio.Detalle_Portafolio(portafolio_actual.get_id_portafolio(), transaccion_creada.get_id_transaccion(), accion.get_cantidad()) """
    controllerDetallePortafolio.crear_detalle_portafolio(detallePortafolio.DetallePortafolio(
        None,
        transaccion_creada.get_cantidad_acciones(),
        accion.get_precio_venta_actual(),
        transaccion_creada.get_fecha_hora(),
        accion,
        inversor.get_portafolio()))
