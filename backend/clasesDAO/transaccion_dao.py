from abc import ABC
import mysql.connector
from backend import interfazDao
from backend import conexion
from negocio import accion, tipoTransaccion, transaccion


class Transaccion_Dao(interfazDao.DataAccesDao):
    def __init__(self):
        pass

    def create(self, objecTransaccion):

        try:
            conn = conexion.connect_to_db()
            cursor = conn.cursor()
            query = """ INSERT INTO transaccion (fecha_hora, 
             cantidad_acciones, 
             precio, 
             comision_broker, 
             inversor_cuit, 
             accion_id_accion, 
             tipo_transaccion_id_tipo_transaccion) 
             VALUES (%s, %s, %s, %s, %s, %s, %s)"""

            cursor.execute(query, (
                objecTransaccion.get_fecha_hora(),
                objecTransaccion.get_cantidad_acciones(),
                objecTransaccion.get_precio(),
                objecTransaccion.get_comision_broker(),
                objecTransaccion.get_inversor_cuit(),
                objecTransaccion.get_accion_id_accion(),
                objecTransaccion.get_tipo_transaccion_id_tipo_transaccion().get_id_tipo_transaccion()))

            conn.commit()
            if cursor.rowcount == 1:
                new_id = cursor.lastrowid
                lastDetallePortafolio = self.get(new_id)
                return lastDetallePortafolio

            else:
                return None
        except mysql.connector.Error as err:
            print("err.")
            raise err

    def get(self, id_transaccion) -> transaccion.Transaccion:
        try:
            conn = conexion.connect_to_db()
            cursor = conn.cursor()
            query = " SELECT * FROM transaccion WHERE id_transaccion= %s"
            cursor.execute(query, (id_transaccion,))
            row = cursor.fetchone()
            conn.commit()
            if row:
                return transaccion.Transaccion(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            else:
                return None
        except mysql.connector.Error as err:
            print("err.")
            raise err

    def get_by_fk(self, id_object):
        id_inversor = (id_object.get_cuit(),)

        try:
            conn = conexion.connect_to_db()
            cursor = conn.cursor()
            query = """SELECT 
                        T.id_transaccion,
                        T.fecha_hora,
                        T.cantidad_acciones,
                        T.precio,                        
                        A.id_accion,
                        A.simbolo,
                        A.nombre,  
                        T.tipo_transaccion_id_tipo_transaccion, 
                        TP.nombre                
                    FROM 
                        transaccion T
                    JOIN accion A ON A.id_accion = T.accion_id_accion
                    JOIN tipo_transaccion TP ON TP.id_tipo_transaccion = T.tipo_transaccion_id_tipo_transaccion
                    where 
                        T.inversor_cuit = %s"""
            cursor.execute(query, id_inversor)
            rows = cursor.fetchall()

            if rows:
                return [transaccion.Transaccion(row[0], row[1], row[2], row[3], None, None,
                        accion.Accion(row[4],row[5],row[6],None,None,None,None,None,None,None,None), tipoTransaccion.TipoTransaccion(row[7],row[8],None)) for row in rows]
            else:
                return None
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            raise
        finally:
            cursor.close()
            conn.close()

    def getAll(self) -> list:
        try:
            conn = conexion.connect_to_db()
            cursor = conn.cursor()
            query = " SELECT * FROM transaccion"
            cursor.execute(query)
            rows = cursor.fetchall()
            if rows:
                return [transaccion.Transaccion(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in rows]
            else:
                return None
        except mysql.connector.Error as err:
            print("err.")
            raise err

    def update(self, transaccion):
        try:
            conn = conexion.connect_to_db()
            cursor = conn.cursor()
            query = " UPDATE transaccion SET fecha_hora=%s, cantidad_acciones=%s, precio=%s, comision_broker=%s WHERE id_transaccion= %s "
            cursor.execute(query, (transaccion.get_fecha_hora(), transaccion.get_cantidad_acciones(
            ), transaccion.get_precio(), transaccion.get_comision_broker()))
            conn.commit()
        except mysql.connector.Error as err:
            print("err.")
            raise err

    def delete(self, id_transaccion):
        try:
            conn = conexion.connect_to_db()
            cursor = conn.cursor()
            query = " DELETE FROM transaccion WHERE id_transaccion= %s"
            cursor.execute(query, (id_transaccion,))
            row = cursor.rowcount
            conn.commit()
            if row > 0:
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print("err.")
            raise err
