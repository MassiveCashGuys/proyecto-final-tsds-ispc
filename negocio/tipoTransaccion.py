class TipoTransaccion:
  
    def __init__(self, id_tipo_transaccion, nombre, descripcion):
        self.__id_tipo_transaccion = id_tipo_transaccion
        self.__nombre = nombre
        self.__descripcion = descripcion

    def get_id_tipo_transaccion(self):
        return self.__id_tipo_transaccion

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_descripcion(self):
        return self.__descripcion

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

