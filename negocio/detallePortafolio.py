class DetallePortafolio:
    def __init__(
            self,             
            id_detalle_portafolio, 
            cantidad_acciones_compradas,
            precio_por_accion, 
            fecha_compra, 
            accion_id_accion, 
            portafolio_id_portafolio):
        
        self.__id_detalle_portafolio = id_detalle_portafolio
        self.__cantidad_acciones_compradas = cantidad_acciones_compradas
        self.__precio_por_accion = precio_por_accion
        self.__fecha_compra = fecha_compra
        self.__accion_id_accion = accion_id_accion  
        self.__portafolio_id_portafolio = portafolio_id_portafolio

    def get_id_detalle_portafolio(self):
        return self.__id_detalle_portafolio
    
    def get_cantidad_acciones_compradas(self):
        return self.__cantidad_acciones_compradas

    def get_precio_por_accion(self):
        return self.__precio_por_accion
    
    def get_fecha_compra(self):
        return self.__fecha_compra

    def get_accion_id_accion(self):
        return self.__accion_id_accion

    def get_portafolio_id_portafolio(self):
        return self.__portafolio_id_portafolio
    
    def set_id_detalle_portafolio(self, id_detalle_portafolio):
        self.__id_detalle_portafolio = id_detalle_portafolio

    def set_cantidad_acciones_compradas(self, cantidad_acciones_compradas):
        self.__cantidad_acciones_compradas = cantidad_acciones_compradas

    def set_precio_por_accion(self, precio_por_accion):
        self.__precio_por_accion = precio_por_accion

    def set_fecha_compra(self, fecha_compra):
        self.__fecha_compra = fecha_compra

    def set_accion_id_accion(self, accion_id_accion):
        self.__accion_id_accion = accion_id_accion

    def set_portafolio_id_portafolio(self, portafolio_id_portafolio):
        self.__portafolio_id_portafolio = portafolio_id_portafolio

    def __str__(self):
        return str(f'Id Detalle Porfolio{self.__id_detalle_portafolio}, Precio por Accion: {self.__precio_por_accion}, Fecha de Compra: {self.__fecha_compra}, Accion: {self.__accion_id_accion}, Portafolio: {self.__portafolio_id_portafolio}')
