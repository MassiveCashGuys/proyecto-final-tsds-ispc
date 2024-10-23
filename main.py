import datetime
from controllers import controllerInicioSesion
from backend.clasesDAO import usuario_dao, transaccion_dao
from negocio import inversor, servicioReglasNegocio, usuario, transaccion, accion, tipoTransaccion
from service import servicioEmail


# from negocio import servicioReglasNegocio

def main():
    controllerInicioSesion.inicio_sesion()


if __name__ == "__main__":
    main()
    

