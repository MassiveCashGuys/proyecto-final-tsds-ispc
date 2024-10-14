import os
from backend.conexion import connect_to_db, disconnect_db


class Portafolio:
    def __init__(self, id_portafolio, saldo_actual, fecha_inicio):
        self.__id_portafolio = id_portafolio
        self.__saldo_actual = saldo_actual
        self.__fecha_inicio = fecha_inicio
        
    def get_saldo_actual(self):
        return self.__saldo_actual;
    
    def set_saldo_actual(self, saldo_actual):
        self.__saldo_actual =saldo_actual;
    
    def get_fecha_inicio(self):
        return self.__fecha_inicio;
    
    def set_fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio =fecha_inicio;
        
    def get_id_portafolio(self):
        return self.__id_portafolio;
    
    def set_id_portafolio(self, id_portafolio):
        self.__id_portafolio =id_portafolio;
        

    def asignar_saldo_inicial(self, idporfolio):
        if connection:
            try:
                cursor = connection.cursor()

                sql = "update portafolio set saldo_actual = %s where id_portafolio= %s"
                values = (1000000, self.__id_portafolio)
                cursor.execute(sql, valores)

                connection.commit()

                cursor.close()
                connection.close()
                return True

            except Exception as e:
                # print(f"Error:{e}")
                return False
        else:
            return "No se pudo conectar a la db"
