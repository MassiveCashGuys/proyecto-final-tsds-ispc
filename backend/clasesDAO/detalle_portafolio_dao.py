import mysql
import mysql.connector
from backend import conexion
from negocio import detallePortafolio, accion


class Detalle_Portafolio_Dao:
    def __init__(self):
        pass

    def create(self, detalle_portafolio):
        try:
            conn = conexion.connect_to_db()
            cursor = conn.cursor()
            query = """ INSERT INTO detalle_portafolio (
            cantidad_acciones_compradas,
            precio_por_accion, 
            fecha_compra, 
            accion_id_accion, 
            portafolio_id_portafolio) 
            VALUES (%s, %s, %s, %s, %s) """

            cursor.execute(query, (
                detalle_portafolio.get_cantidad_acciones_compradas(),
                detalle_portafolio.get_precio_por_accion(),
                detalle_portafolio.get_fecha_compra(),
                detalle_portafolio.get_accion_id_accion().get_id_accion(),
                detalle_portafolio.get_portafolio_id_portafolio()
            ))

            conn.commit()
            if cursor.rowcount == 1:
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print("err.")
            raise err

    def get(self, id_detalle_portafolio):
        try:
            conn = conexion.connect_to_db()
            cursor = conn.cursor()
            query = " SELECT * FROM detalle_portafolio WHERE id_detalle_portafolio= %s"
            cursor.execute(query, (id_detalle_portafolio,))
            row = cursor.fetchone()
            conn.commit()
            if row:
                return detallePortafolio.DetallePortafolio(row[0], row[1], row[2], row[3], row[4], row[5])
            else:
                return None
        except mysql.connector.Error as err:
            print("err.")
            raise err

    def get_by_fk(self, id_object) -> list:

        try:
            conn = conexion.connect_to_db()
            cursor = conn.cursor()

            query = """	
	                     Select DP.id_detalle_portafolio, SUM(DP.cantidad_acciones_compradas) as cantidad_acciones_compradas,
                       DP.precio_por_accion,DP.fecha_compra, A.id_accion, A.simbolo, A.nombre, A.cantidad, A.precio_venta_actual, A.minimo_diario,
                       A.maximo_diario, DP.portafolio_id_portafolio   
                       FROM detalle_portafolio as DP
	                     INNER JOIN accion as A ON DP.accion_id_accion = A.id_accion
                       where DP.portafolio_id_portafolio = %s 
                       GROUP BY A.simbolo
                    """
            cursor.execute(query,
                           id_object
                           )
            rows = cursor.fetchall()
            if rows:
                return [detallePortafolio.DetallePortafolio(row[0], row[1], row[2], row[3], accion.Accion(row[4], row[5], row[6], row[7], row[8], None, None, row[9], row[10], None, None), row[11]) for row in rows]
            else:
                return None

        except mysql.connector.Error as err:
            print("err.")
            raise err

    def getAll(self) -> list:
        try:
            conn = conexion.connect_to_db()
            cursor = conn.cursor()
            query = " SELECT * FROM detalle_portafolio"
            cursor.execute(query)
            rows = cursor.fetchall()
            if rows:
                return [detallePortafolio.DetallePortafolio(row[0], row[1], row[2], row[3], row[4], row[5]) for row in rows]
            else:
                return None
        except mysql.connector.Error as err:
            print("err.")
            raise err

    def update(self, detalle_portafolio):
        try:
            conn = conexion.connect_to_db()
            cursor = conn.cursor()
            query = " UPDATE detalle_portafolio SET cantidad_acciones_compradas=%s,precio_por_accion=%s, fecha_compra=%s, accion_id_accion=%s, portafolio_id_portafolio=%s WHERE id_detalle_portafolio= %s "
            cursor.execute(query, (
                detalle_portafolio.get_cantidad_acciones_compradas(),
                detalle_portafolio.get_precio_por_accion(),
                detalle_portafolio.get_fecha_compra(),
                detalle_portafolio.get_accion_id_accion().get_id_accion(),
                detalle_portafolio.get_portafolio_id_portafolio().get_id_portafolio(),
                detalle_portafolio.get_id_detalle_portafolio()
            ))
            conn.commit()
        except mysql.connector.Error as err:
            print("err.")
            raise err

    def delete(self, id_detalle_portafolio):
        try:
            conn = conexion.connect_to_db()
            cursor = conn.cursor()
            query = " DELETE FROM detalle_portafolio WHERE id_detalle_portafolio= %s"
            cursor.execute(query, (id_detalle_portafolio,))
            row = cursor.fetchone()
            conn.commit()
            if row > 0:
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print("err.")
            raise err
