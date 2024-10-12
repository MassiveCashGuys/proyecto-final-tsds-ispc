import os
from backend.conexion import connect_to_db, disconnect_db


class Porfolio:
    def __init__(self, idporfolio):
        self.__id_portafolio = idporfolio

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
