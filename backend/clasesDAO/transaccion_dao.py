from abc import ABC
import mysql.connector
from backend import interfazDao
from backend import conexion
from negocio import transaccion

class Transaccion_Dao(interfazDao.DataAccesDao):
    def __init__(self):
        pass
    
    
    def create(self,transaccion):
      
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" INSERT INTO transaccion (fecha_hora, cantidad_acciones, precio, comision_broker) VALUES (%s, %s, %s, %s)"
             cursor.execute(query,(transaccion.get_fecha_hora(),transaccion.get_cantidad_acciones(),transaccion.get_precio(),transaccion.get_comision_broker()))
             conn.commit()
             if cursor.rowcount == 1:
                return True
             else:
                return False
         except mysql.connector.Error as err:
             print("err.")
             raise err

 
    def get(self, id_transaccion)->transaccion.Transaccion:
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" SELECT * FROM transaccion WHERE id_transaccion= %s"
             cursor.execute(query,(id_transaccion,))
             row = cursor.fetchone()
             conn.commit()
             if row:
                return transaccion.Transaccion(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
             else:
                return None
         except mysql.connector.Error as err:
             print("err.")
             raise err 
        
    
    def getAll(self)->list:
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" SELECT * FROM transaccion"
             cursor.execute(query)
             rows = cursor.fetchall()
             if rows:
                return [transaccion.Transaccion(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]) for row in rows]
             else:
                return None
         except mysql.connector.Error as err:
             print("err.")
             raise err 
        
    
    def update(self, transaccion):
         try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" UPDATE transaccion SET fecha_hora=%s, cantidad_acciones=%s, precio=%s, comision_broker=%s WHERE id_transaccion= %s "
             cursor.execute(query,(transaccion.get_fecha_hora(),transaccion.get_cantidad_acciones(),transaccion.get_precio(),transaccion.get_comision_broker()))
             conn.commit()
         except mysql.connector.Error as err:
             print("err.")
             raise err 

    
    def delete(self, id_transaccion):
        try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" DELETE FROM transaccion WHERE id_transaccion= %s"
             cursor.execute(query,(id_transaccion,))
             row = cursor.rowcount
             conn.commit()
             if row > 0:
                return True
             else:
                return False
        except mysql.connector.Error as err:
             print("err.")
             raise err 
        
    

   
   