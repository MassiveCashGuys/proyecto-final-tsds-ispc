import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Crear el mensaje
def crear_mensaje():
    remitente = 'argbrokerLegal@gmail.com'
    destinatario = 'programacionwebolmos@gmail.com'
    contraseña = 'yvcg xekw gdmn kzbt'  # Usa la contraseña de aplicación aquí

    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = 'Recuperación de contraseña'

    # Contenido del correo
    cuerpo = 'Este es el contenido del correo'
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Conexión con el servidor SMTP de Gmail
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()  # Iniciar TLS para asegurar la conexión
        servidor.login(remitente, contraseña)
        servidor.sendmail(remitente, destinatario, mensaje.as_string())
        servidor.quit()
        print("Correo enviado exitosamente.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")


