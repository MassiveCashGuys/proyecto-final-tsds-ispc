import os
from backend.conexion import connect_to_db, disconnect_db

if __name__ == "__main__":
    connection = connect_to_db()

# Ej de query
"""
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("Select * from desprogramadores")
            result = cursor.fetchall()

            for desprogramador in result:
                print(desprogramador)

        except Exception as e:
            print(f"Tu query es un asco:{e}")
    else:
        print("No se pudo conectar a la db")
"""
