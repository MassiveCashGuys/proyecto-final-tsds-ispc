from abc import ABC
import mysql.connector
from backend import interfazDao
from backend import conexion
from negocio import tipoTransaccion

class Tipo_Transaccion_Dao(interfazDao.DataAccesDao):
    def __init__(self):
        pass
    
    def create(self,tipo_transaccion):
      
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" INSERT INTO tipo_transaccion (nombre, descripcion) VALUES (%s, %s)"
             cursor.execute(query,(tipo_transaccion.get_nombre(),tipo_transaccion.get_descripcion()))
             conn.commit()
             if cursor.rowcount == 1:
                return True
             else:
                return False
         except mysql.connector.Error as err:
             print("err.")
             raise err 

 
    def get(self, id_tipo_transaccion)->tipoTransaccion.TipoTransaccion:
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" SELECT * FROM tipo_transaccion WHERE id_tipo_transaccion= %s"
             cursor.execute(query,(id_tipo_transaccion,))
             row = cursor.fetchone()
             conn.commit()
             if row:
                return tipoTransaccion.TipoTransaccion(row[0],row[1],row[2])
             else:
                return None
         except mysql.connector.Error as err:
             print("err.")
             raise err 
        
 
    def getAll(self)->list:
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" SELECT * FROM tipo_transaccion"
             cursor.execute(query)
             rows = cursor.fetchall()
             if rows:
                return [tipoTransaccion.TipoTransaccion(row[0],row[1],row[2]) for row in rows]
             else:
                return None
         except mysql.connector.Error as err:
             print("err.")
             raise err 
        
  
    def update(self, tipo_transaccion):
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" UPDATE tipo_transaccion SET nombre=%s, descripcion=%s WHERE id_tipo_transaccion= %s "
             cursor.execute(query,(tipo_transaccion.get_nombre(),tipo_transaccion.get_descripcion(), tipo_transaccion.get_id_tipo_documento()))
             conn.commit()
         except mysql.connector.Error as err:
             print("err.")
             raise err 

    
    def delete(self, id_tipo_transaccion):
        try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" DELETE FROM tipo_transaccion WHERE id_tipo_transaccion= %s"
             cursor.execute(query,(id_tipo_transaccion,))
             row = cursor.rowcount
             conn.commit()
             if row > 0:
                return True
             else:
                return False
        except mysql.connector.Error as err:
             print("err.")
             raise err 
        
    

   
   