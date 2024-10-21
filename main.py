from controllers import controllerInicioSesion
from backend.clasesDAO import usuario_dao
from negocio import servicioReglasNegocio, usuario
from service import servicioEmail


# from negocio import servicioReglasNegocio


def main():
    controllerInicioSesion.inicio_sesion()

if __name__ == "__main__":
    main()
