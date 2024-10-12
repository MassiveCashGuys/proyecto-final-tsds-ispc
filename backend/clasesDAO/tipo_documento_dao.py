from abc import ABC, abstractmethod
import mysql.connector
from mysql.connector import errorcode
from backend import interfazDao
from backend import conexion

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

 
    def get(self, id_object):
        pass

  
    def update(self, object):
        pass

    
    def delete(self, id_object):
        pass

   
   