from abc import ABC
import mysql.connector
from backend import interfazDao
from backend import conexion
from negocio import empresa

class empresaDao(interfazDao.DataAccesDao):
    def __init__(self):
        pass
    
    def create(self,objectempresa):
      
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" INSERT INTO empresa (cuit, numero_documento, nombre, apellido, id_portafolio, id_tipo_empresa, id_tipo_documento, id_usuario ) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)"
             cursor.execute(query,(objectempresa.get_cuit(), objectempresa.get_numero_documento(), objectempresa.get_nombre(), objectempresa.get_apellido(), objectempresa.get_portafolio().get_id_portafolio(), objectempresa.get_tipo_empresa().get_id_tipo_empresa(), objectempresa.get_tipo_documento().get_id_tipo_documento(), objectempresa.get_user().get_id_user()))
             conn.commit()
             if cursor.rowcount == 1:
                  lastempresa = self.get(objectempresa.get_cuit())
                  return lastempresa
             else:
                return False
         except mysql.connector.Error as err:
             print("err.")
             raise err 

 
    def get(self, id_object_empresa)->empresa.Empresa:
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" SELECT * FROM empresa WHERE id_empresa= %s"
             cursor.execute(query,(id_object_empresa,))
             row = cursor.fetchone()
             conn.commit()
             if row:
                return empresa.empresa(row[0],row[1],row[2],row[3])
             else:
                return None
         except mysql.connector.Error as err:
             print("err.")
             raise err 
    
    def get_by_fk(self, fk_objectempresa)->empresa.Empresa:
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" SELECT * FROM empresa WHERE id_usuario= %s"
             cursor.execute(query,(fk_objectempresa,))
             row = cursor.fetchone()
             conn.commit()
             if row:
                return empresa.empresa(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
             else:
                return None
         except mysql.connector.Error as err:
             print("err.")
             raise err   
 
    def getAll(self)->list:
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" SELECT * FROM empresa"
             cursor.execute(query)
             rows = cursor.fetchall()
             if rows:
                return [empresa.Empresa(row[0],row[1],row[2]) for row in rows]
             else:
                return None
         except mysql.connector.Error as err:
             print("err.")
             raise err 
        
  
    def update(self, objectempresa):
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" UPDATE empresa SET nombre = %s, apellido = %s, id_portafolio = %s, id_tipo_empresa = %s, id_tipo_documento = %s"
             cursor.execute(query,(objectempresa.get_nombre(),objectempresa.get_descripcion(), objectempresa.get_id_tipo_documento()))
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
        
    

   
   