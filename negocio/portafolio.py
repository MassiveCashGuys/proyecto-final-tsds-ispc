class Portafolio:
    def __init__(self, id_portafolio, saldo_actual, fecha_inicio):
        self.__id_portafolio = id_portafolio
        self.__saldo_actual = saldo_actual
        self.__fecha_inicio = fecha_inicio

    def get_saldo_actual(self):
        return self.__saldo_actual

    def set_saldo_actual(self, saldo_actual):
        self.__saldo_actual = saldo_actual

    def get_fecha_inicio(self):
        return self.__fecha_inicio

    def set_fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    def get_id_portafolio(self):
        return self.__id_portafolio

    def set_id_portafolio(self, id_portafolio):
        self.__id_portafolio = id_portafolio
