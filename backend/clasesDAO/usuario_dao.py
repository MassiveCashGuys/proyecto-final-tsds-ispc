# 
from abc import ABC
import mysql.connector
from backend import interfazDao
from backend import conexion



class Usuario_Dao(interfazDao.DataAccesDao):
    def __init__(self):
        pass


    def create(self,user):
        try:
             conn = conexion.connect_to_db()
             cursor = conn.cursor()
             query=" INSERT INTO usuario (id_user, password, id_perfil) VALUES (%s, %s, %s)" # ponerlo igual que en la base de datos
             cursor.execute(query,(user.get_id_user(), user.get_password(), user.get_id_perfil())) # hacer geters y seters del metodo usuario
             conn.commit()
             if cursor.rowcount == 1:
                return True
             else:
                return False
        except mysql.connector.Error as err:
             print("err.")
             raise err 
    
    def get(self, usuario): #fijarse que este igual en la base de datos!!!
        pass
    
    
    def getAll(self):
        pass

    
    def update(self, usuario):
        pass

    
    def delete(self, usuario):
        pass
