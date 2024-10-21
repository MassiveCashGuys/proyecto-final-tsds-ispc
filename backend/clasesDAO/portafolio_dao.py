from abc import ABC
import mysql.connector
from backend import interfazDao
from backend import conexion
from negocio import portafolio


class Portafolio_Dao(interfazDao.DataAccesDao):
    def __init__(self):
        pass

    def create(self, objectPortafolio):

        try:
            conn = conexion.connect_to_db()
            cursor = conn.cursor()
            query = " INSERT INTO portafolio (saldo_actual, fecha_inicio) VALUES (%s, %s)"
            cursor.execute(query, (objectPortafolio.get_saldo_actual(),
                           objectPortafolio.get_fecha_inicio()))
            conn.commit()
            if cursor.rowcount == 1:
                new_id = cursor.lastrowid
                lastPortafolio = self.get( new_id)
                return lastPortafolio
            else:
                return None
        except mysql.connector.Error as err:
            print("err.")
            raise err

    def get(self, id_portafolio) -> portafolio.Portafolio:
        try:
            conn = conexion.connect_to_db()
            cursor = conn.cursor()
            query = " SELECT * FROM portafolio WHERE id_portafolio= %s"
            cursor.execute(query, (id_portafolio,))
            row = cursor.fetchone()
            conn.commit()
            if row:
                return portafolio.Portafolio(row[0], row[1], row[2])
            else:
                return None
        except mysql.connector.Error as err:
            print("err.")
            raise err

    def getAll(self) -> list:
        try:
            conn = conexion.connect_to_db()
            cursor = conn.cursor()
            query = " SELECT * FROM portafolio"
            cursor.execute(query)
            rows = cursor.fetchall()
            if rows:
                return [portafolio.Portafolio(row[0], row[1], row[2]) for row in rows]
            else:
                return None
        except mysql.connector.Error as err:
            print("err.")
            raise err

    def update(self, portafolio, saldo):
        try:
            conn = conexion.connect_to_db()
            cursor = conn.cursor()
            query = " UPDATE portafolio SET saldo_actual=%s  WHERE id_portafolio= %s "
            cursor.execute(query, (saldo, portafolio))
            conn.commit()
        except mysql.connector.Error as err:
            print("err.")
            raise err

    def delete(self, id_portafolio):
        try:
            conn = conexion.connect_to_db()
            cursor = conn.cursor()
            query = " DELETE FROM portafolio WHERE id_portafolio= %s"
            cursor.execute(query, (id_portafolio,))
            row = cursor.rowcount
            conn.commit()
            if row > 0:
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print("err.")
            raise err
