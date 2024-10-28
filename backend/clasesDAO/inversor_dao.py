from abc import ABC
import mysql.connector
from backend import interfazDao
from backend import conexion
from negocio import inversor, portafolio

class InversorDao(interfazDao.DataAccesDao):
    def __init__(self):
        pass
    
    def create(self, objectInversor)->inversor.Inversor:
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             cursor.execute("START TRANSACTION;")
             cursor.execute("""
                    INSERT INTO usuario (id_user, password, id_perfil) 
                    VALUES (%s, %s, %s);
                """, (objectInversor.get_user().get_id_user(), objectInversor.get_user().get_password(), objectInversor.get_user().get_id_perfil()))

             id_usuario = objectInversor.get_user().get_id_user() 
             cursor.execute("""
                    INSERT INTO portafolio (saldo_actual, fecha_inicio) 
                    VALUES (%s, %s);
                """, (objectInversor.get_portafolio().get_saldo_actual(), objectInversor.get_portafolio().get_fecha_inicio())) 
             
             id_portafolio = cursor.lastrowid  
             cursor.execute("""
                INSERT INTO inversor (cuit, numero_documento, nombre, apellido, id_portafolio, id_tipo_inversor, id_tipo_documento, id_usuario) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """, (objectInversor.get_cuit(),
                  objectInversor.get_numero_documento(),
                  objectInversor.get_nombre(),
                  objectInversor.get_apellido(), 
                  id_portafolio,
                  objectInversor.get_tipo_inversor().get_id_tipo_inversor(),
                  objectInversor.get_tipo_documento().get_id_tipo_documento(),
                  id_usuario))
             
             conn.commit()
             if cursor.rowcount == 1:
                  lastInversor = self.get(objectInversor.get_cuit())
                  print(f'Los datos se guardaron correctamente.')
                  return lastInversor
             else:
                return False
        
         except mysql.connector.Error as err:
    
             print(f"Error: {err}")             
             conexion.rollback()
             raise err 

 
    def get(self, id_objectInversor)->inversor.Inversor:
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" SELECT * FROM inversor WHERE cuit= %s"
             cursor.execute(query,(id_objectInversor,))
             row = cursor.fetchone()
             conn.commit()
             if row:
                return inversor.Inversor(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
             else:
                return None
         except mysql.connector.Error as err:
             print("err.")
             raise err 
    
    def get_by_fk(self, fk_objectInversor)->inversor.Inversor:
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=""" SELECT I.cuit, I.numero_documento, I.nombre, I.apellido, P.id_portafolio, P.saldo_actual, P.fecha_inicio, I.id_tipo_inversor, I.id_tipo_documento, I.id_usuario
                        FROM inversor I
                        JOIN portafolio P ON P.id_portafolio = I.id_portafolio
                        WHERE I.id_usuario =  %s"""
             cursor.execute(query,(fk_objectInversor,))
             row = cursor.fetchone()
             conn.commit()
             if row:
                return inversor.Inversor(row[0],row[1],row[2],row[3],portafolio.Portafolio(row[4],row[5],row[6]),row[7],row[8],row[9])
             else:
                return None
         except mysql.connector.Error as err:
             print("err.")
             raise err   
 
    def getAll(self)->list:
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" SELECT * FROM inversor"
             cursor.execute(query)
             rows = cursor.fetchall()
             if rows:
                return [inversor.Inversor(row[0],row[1],row[2]) for row in rows]
             else:
                return None
         except mysql.connector.Error as err:
             print("err.")
             raise err 
        
  
    def update(self, objectInversor):
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" UPDATE inversor SET nombre = %s, apellido = %s, id_portafolio = %s, id_tipo_inversor = %s, id_tipo_documento = %s"
             cursor.execute(query,(objectInversor.get_nombre(),objectInversor.get_descripcion(), objectInversor.get_id_tipo_documento()))
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
        
    
    
