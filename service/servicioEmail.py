import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import string
from dotenv import load_dotenv

   

# Crear el mensaje
def crear_mensaje(dato):
    load_dotenv()
    remitente =  os.getenv("REMITENTE")
    destinatario = dato['usuario'].get_id_user()
    contraseña = os.getenv("EMAIL_PASSWORD") 
  

    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = 'Recuperación de contraseña'

    cuerpo = f'En este mail le pasamos la contraseña para poder logearse. Su contraseña es: {dato["password"]} se recomienda modificar la contraseña.'
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()  
        servidor.login(remitente, contraseña)
        servidor.sendmail(remitente, destinatario, mensaje.as_string())
        servidor.quit()
        print("Su contraseña se envio a su email.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")


def generar_contrasena(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena
