import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv();

conexion = mysql.connector.connect(
    user = os.getenv("USER"),
    password = os.getenv("PASSWORD"),
    host = os.getenv("HOST"),
    database= os.getenv("DATABASE"),
    port= os.getenv("PORT")
);

cursor = conexion.cursor();
query = "SHOW TABLES";
cursor.execute(query)

tablas = cursor.fetchall()
for tabla in tablas:
    print(tabla[0])

cursor.close();
conexion.close();