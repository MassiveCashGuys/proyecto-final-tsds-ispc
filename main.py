import os
from backend.conexion import connect_to_db, disconnect_db

if __name__ == "__main__":
    con_ok = connect_to_db()
    print(f"Se conecto???: {con_ok}")
