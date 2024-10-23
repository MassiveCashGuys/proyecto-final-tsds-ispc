import datetime
from controllers import controllerInicioSesion
from backend.clasesDAO import usuario_dao, transaccion_dao
from negocio import inversor, portafolio, servicioReglasNegocio, usuario, transaccion, accion, tipoTransaccion
from negocio import detallePortafolio
from backend.clasesDAO import detalle_portafolio_dao, portafolio_dao
from service import servicioEmail


# from negocio import servicioReglasNegocio

def main():
    controllerInicioSesion.inicio_sesion()


if __name__ == "__main__":
    main()
    

