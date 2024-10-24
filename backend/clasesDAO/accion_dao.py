from abc import ABC
import mysql.connector
from backend import interfazDao
from backend import conexion
from negocio import accion, empresa

class AccionDao(interfazDao.DataAccesDao):
    def __init__(self):
        pass
    
    def create(self,objectaccion):
      
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" INSERT INTO accion ( simbolo, nombre, cantidad, precio_venta_actual, cantidad_venta_diaria, fecha_apertura, minimo_diario, maximo_diario, ultimo_cierre, id_empresa ) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)"
             cursor.execute(query,())
             conn.commit()
             if cursor.rowcount == 1:
                  lastaccion = self.get(objectaccion.get_cuit())
                  return lastaccion
             else:
                return False
         except mysql.connector.Error as err:
             print("err.")
             raise err 

 
    def get(self, id_objectaccion)->accion.Accion:
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" SELECT * FROM accion WHERE cuit= %s"
             cursor.execute(query,(id_objectaccion,))
             row = cursor.fetchone()
             conn.commit()
             if row:
                return accion.accion(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
             else:
                return None
         except mysql.connector.Error as err:
             print("err.")
             raise err 
    
    def get_by_fk(self, fk_objectaccion)->accion.Accion:
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" SELECT * FROM accion WHERE id_usuario= %s"
             cursor.execute(query,(fk_objectaccion,))
             row = cursor.fetchone()
             conn.commit()
             if row:
                return accion.Accion(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
             else:
                return None
         except mysql.connector.Error as err:
             print("err.")
             raise err   
 
    def getAll(self)->list:
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query = """
                 SELECT A.id_accion, A.simbolo, A.nombre, A.cantidad,
                 A.precio_venta_actual, A.cantidad_venta_diaria,
                 A.fecha_apertura, A.minimo_diario, A.maximo_diario, A.ultimo_cierre, E.id_empresa, E.nombre,
                 E.razon_social, E.descripcion
                 FROM accion A
                 JOIN empresa E ON A.id_empresa = E.id_empresa where A.cantidad > 0
             """
             cursor.execute(query)
             rows = cursor.fetchall()
             if rows:
                return [accion.Accion(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],empresa.Empresa(row[10],row[11],row[12],row[13])) for row in rows]
             else:
                return None
         except mysql.connector.Error as err:
             print("err.")
             raise err 
        
  
    def update(self, object_accion):
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=""" UPDATE accion SET  simbolo = %s, nombre = %s, cantidad = %s,
                precio_venta_actual = %s, cantidad_venta_diaria = %s,
                fecha_apertura = %s, minimo_diario = %s, maximo_diario = %s, ultimo_cierre = %s, id_empresa = %s WHERE id_accion = %s""" 
             cursor.execute(query,(object_accion.get_simbolo(),
                                   object_accion.get_nombre(),
                                   object_accion.get_cantidad(),
                object_accion.get_precio_venta_actual(),
                object_accion.get_cantidad_venta_diaria(),
                object_accion.getFecha_apertura(),
                object_accion.get_minimo_diario(),
                object_accion.get_maximo_diario(),
                object_accion.get_ultimo_cierre(),
                object_accion.get_id_empresa().get_id_empresa(),
                object_accion.get_id_accion()))
             conn.commit()
         except mysql.connector.Error as err:
             print("err.")
             raise err 

    
    def delete(self, cuit):
        try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" DELETE FROM cuit WHERE cuit = %s"
             cursor.execute(query,(cuit,))
             row = cursor.rowcount
             conn.commit()
             if row > 0:
                return True
             else:
                return False
        except mysql.connector.Error as err:
             print("err.")
             raise err 
        
    

   
   