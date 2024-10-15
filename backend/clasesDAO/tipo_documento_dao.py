from abc import ABC
import mysql.connector
from backend import interfazDao
from backend import conexion
from negocio import tipoDocumento

class Tipo_Documento_Dao(interfazDao.DataAccesDao):
    def __init__(self):
        pass
    
    def create(self,tipo_documento):
      
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" INSERT INTO tipo_documento (nombre, descripcion) VALUES (%s, %s)"
             cursor.execute(query,(tipo_documento.get_nombre(),tipo_documento.get_descripcion()))
             conn.commit()
             if cursor.rowcount == 1:
                return True
             else:
                return False
         except mysql.connector.Error as err:
             print("err.")
             raise err 

 
    def get(self, id_tipo_documento)->tipoDocumento.TipoDocumento:
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" SELECT * FROM tipo_documento WHERE id_tipo_documento= %s"
             cursor.execute(query,(id_tipo_documento,))
             row = cursor.fetchone()
             conn.commit()
             if row:
                return tipoDocumento.TipoDocumento(row[0],row[1],row[2])
             else:
                return None
         except mysql.connector.Error as err:
             print("err.")
             raise err 
        
 
    def getAll(self)->list:
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" SELECT * FROM tipo_documento"
             cursor.execute(query)
             rows = cursor.fetchall()
             if rows:
                return [tipoDocumento.TipoDocumento(row[0],row[1],row[2]) for row in rows]
             else:
                return None
         except mysql.connector.Error as err:
             print("err.")
             raise err 
        
  
    def update(self, tipo_documento):
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" UPDATE tipo_documento SET nombre=%s, descripcion=%s WHERE id_tipo_documento= %s "
             cursor.execute(query,(tipo_documento.get_nombre(),tipo_documento.get_descripcion(), tipo_documento.get_id_tipo_documento()))
             conn.commit()
         except mysql.connector.Error as err:
             print("err.")
             raise err 

    
    def delete(self, id_tipo_documento):
        try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" DELETE FROM tipo_documento WHERE id_tipo_documento= %s"
             cursor.execute(query,(id_tipo_documento,))
             row = cursor.rowcount
             conn.commit()
             if row > 0:
                return True
             else:
                return False
        except mysql.connector.Error as err:
             print("err.")
             raise err 
        
    

   
   