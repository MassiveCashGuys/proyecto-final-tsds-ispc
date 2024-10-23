from controllers import controllerInicioSesion
from backend.clasesDAO import usuario_dao
from negocio import servicioReglasNegocio, usuario
from service import servicioEmail


# from negocio import servicioReglasNegocio

"""user = usuario.Usuario("gusta@gmail.com", servicioReglasNegocio.crear_encriptacion_password("Gusta3729"),1)
print(user)
print(controllerInicioSesion.crear_usuario(user))"""

def main():
    controllerInicioSesion.inicio_sesion()

if __name__ == "__main__":
    main()