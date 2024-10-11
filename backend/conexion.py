import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()


def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DATABASE"),
            port=os.getenv("PORT"),
        )

        if connection.is_connected():
            return True
            # return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return False


def disconnect_db():
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Conexión cerrada")
