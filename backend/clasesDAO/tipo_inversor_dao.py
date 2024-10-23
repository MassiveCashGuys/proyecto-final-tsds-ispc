from abc import ABC
import mysql.connector
from backend import interfazDao
from backend import conexion
from negocio import tipoInversor

class Tipo_Inversor_Dao(interfazDao.DataAccesDao):
    def __init__(self):
        pass
    
    def create(self,tipo_inversor):
      
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" INSERT INTO tipo_inversor (nombre, descripcion) VALUES (%s, %s)"
             cursor.execute(query,(tipo_inversor.get_nombre(),tipo_inversor.get_descripcion()))
             conn.commit()
             if cursor.rowcount == 1:
                return True
             else:
                return False
         except mysql.connector.Error as err:
             print("err.")
             raise err 

 
    def get(self, id_tipo_inversor)->tipoInversor.TipoInversor:
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" SELECT * FROM tipo_inversor WHERE id_tipo_inversor= %s"
             cursor.execute(query,(id_tipo_inversor,))
             row = cursor.fetchone()
             conn.commit()
             if row:
                return tipoInversor.TipoInversor(row[0],row[1],row[2])
             else:
                return None
         except mysql.connector.Error as err:
             print("err.")
             raise err 
       
 
    def getAll(self)->list:
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" SELECT * FROM tipo_inversor"
             cursor.execute(query)
             rows = cursor.fetchall()
             if rows:
                return [tipoInversor.TipoInversor(row[0],row[1],row[2]) for row in rows]
             else:
                return None
         except mysql.connector.Error as err:
             print("err.")
             raise err 
        
  
    def update(self, tipo_inversor):
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" UPDATE tipo_inversor SET nombre=%s, descripcion=%s WHERE id_tipo_inversor= %s "
             cursor.execute(query,(tipo_inversor.get_nombre(),tipo_inversor.get_descripcion(), tipo_inversor.get_id_tipo_documento()))
             conn.commit()
         except mysql.connector.Error as err:
             print("err.")
             raise err 

    
    def delete(self, id_tipo_inversor):
        try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" DELETE FROM tipo_inversor WHERE id_tipo_inversor= %s"
             cursor.execute(query,(id_tipo_inversor,))
             row = cursor.rowcount
             conn.commit()
             if row > 0:
                return True
             else:
                return False
        except mysql.connector.Error as err:
             print("err.")
             raise err 
        
    

   
   