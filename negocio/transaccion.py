class Transaccion:   
    def __init__(self, id_transaccion, fecha_hora, cantidad_acciones, precio, comision_broker, inversor_cuit, accion_id_accion, tipo_transaccion_id_tipo_transaccion):
        self.__id_transaccion = id_transaccion
        self.__fecha_hora = fecha_hora
        self.__cantidad_acciones = cantidad_acciones
        self.__precio = precio
        self.__comision_broker = comision_broker
        self.__inversor_cuit = inversor_cuit
        self.__accion_id_accion = accion_id_accion
        self.__tipo_transaccion_id_tipo_transaccion = tipo_transaccion_id_tipo_transaccion

    def get_id_transaccion(self):
        return self.__id_transaccion
    
    def get_fecha_hora(self):
        return self.__fecha_hora
    
    def get_cantidad_acciones(self):
        return self.__cantidad_acciones
    
    def get_precio(self):
        return self.__precio
    
    def get_comision_broker(self):
        return self.__comision_broker
    
    def get_inversor_cuit(self):
        return self.__inversor_cuit
    
    def get_accion_id_accion(self):
        return self.__accion_id_accion
    
    def get_tipo_transaccion_id_tipo_transaccion(self):
        return self.__tipo_transaccion_id_tipo_transaccion
    
    def set_id_transaccion(self, id_transaccion):
        self.__id_transaccion = id_transaccion
    
    def set_fecha_hora(self, fecha_hora):
        self.__fecha_hora = fecha_hora
    
    def set_cantidad_acciones(self, cantidad_acciones):
        self.__cantidad_acciones = cantidad_acciones
    
    def set_precio(self, precio):
        self.__precio = precio
    
    def set_comision_broker(self, comision_broker):
        self.__comision_broker = comision_broker
    
    def set_inversor_cuit(self, inversor_cuit):
        self.__inversor_cuit = inversor_cuit
    
    def set_accion_id_accion(self, accion_id_accion):
        self.__accion_id_accion = accion_id_accion
    
    def set_tipo_transaccion_id_tipo_transaccion(self, tipo_transaccion_id_tipo_transaccion):
        self.__tipo_transaccion_id_tipo_transaccion = tipo_transaccion_id_tipo_transaccion

    def __str__(self):
        return str(f'Numero de transacció: {self.get_id_transaccion()}, Fecha:{self.get_fecha_hora()}, Cantidad:{self.get_cantidad_acciones()}, Precio:{self.get_precio()}, Comisión: {self.get_comision_broker()}, Ciut: {self.get_inversor_cuit()}, Acción: {self.get_accion_id_accion()}, id Transacción:{self.get_tipo_transaccion_id_tipo_transaccion()}')
