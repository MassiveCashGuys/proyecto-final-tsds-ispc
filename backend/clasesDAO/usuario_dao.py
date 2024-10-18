from abc import ABC
import mysql.connector
from backend import interfazDao
from backend import conexion
from negocio import usuario



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
    
    def get(self, id_user) -> usuario.Usuario:
        try:
            conn = conexion.connect_to_db()
            cursor = conn.cursor()
            query = "SELECT * FROM usuario WHERE id_user = %s"
            cursor.execute(query, (id_user,))
            row = cursor.fetchone()
            if row:
                return usuario.Usuario(row[0], row[1], row[2])
            else:
                return None
        except mysql.connector.Error as err:
            print("Error:", err)
            raise err
    
    
    def getAll(self) -> list:
        try:
            conn = conexion.connect_to_db()
            cursor = conn.cursor()
            query = "SELECT * FROM usuario"
            cursor.execute(query)
            rows = cursor.fetchall()
            if rows:
                return [usuario.Usuario(row[0], row[1], row[2]) for row in rows]
            else:
                return None
        except mysql.connector.Error as err:
            print("err.")
            raise err

    
    def update(self, user):
        try:
            conn = conexion.connect_to_db()
            cursor = conn.cursor()
            query = "UPDATE usuario SET password=%s, id_perfil=%s WHERE id_user=%s"
            cursor.execute(query, (user.get_password(), user.get_id_perfil(), user.get_id_user()))
            conn.commit()
        except mysql.connector.Error as err:
            print("err.")
            raise err

    
    def delete(self, id_user):
        try:
            conn = conexion.connect_to_db()
            cursor = conn.cursor()
            query = "DELETE FROM usuario WHERE id_user = %s"
            cursor.execute(query, (id_user,))
            row = cursor.rowcount
            conn.commit()
            if row > 0:
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print("err.")
            raise err 
