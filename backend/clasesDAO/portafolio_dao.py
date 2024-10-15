from abc import ABC
import mysql.connector
from backend import interfazDao
from backend import conexion
from negocio import tipoDocumento


class Portafolio_Dao(interfazDao.DataAccesDao):
    def __init__(self):
        pass

    def create(self, portafolio):

        try:
            conn = conexion.connect_to_db()
            cursor = conn.cursor()
            query = " INSERT INTO portafolio (nombre, descripcion) VALUES (%s, %s)"
            cursor.execute(query, (portafolio.get_saldo_inicial(),
                           portafolio.get_fecha_inicio()))
            conn.commit()
            if cursor.rowcount == 1:
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print("err.")
            raise err

    def get(self, id_portafolio) -> tipoDocumento.TipoDocumento:
        try:
            conn = conexion.connect_to_db()
            cursor = conn.cursor()
            query = " SELECT * FROM portafolio WHERE id_portafolio= %s"
            cursor.execute(query, (id_portafolio,))
            row = cursor.fetchone()
            conn.commit()
            if row:
                return tipoDocumento.TipoDocumento(row[0], row[1], row[2])
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
                return [tipoDocumento.TipoDocumento(row[0], row[1], row[2]) for row in rows]
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
