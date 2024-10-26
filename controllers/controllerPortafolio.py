from backend.clasesDAO import portafolio_dao
from negocio import portafolio, servicioReglasNegocio


def cargar_saldo_inicial(id_portafolio):
    aux = portafolio_dao.Portafolio_Dao()
    aux.update(saldo=1000000, portafolio=id_portafolio)


def crear_portafolio() -> portafolio.Portafolio:
    nuevo_portafolio_dao = portafolio_dao.Portafolio_Dao()
    nuevoPortafolio = portafolio.Portafolio(
        None, 0, servicioReglasNegocio.definir_fecha_actual(servicioReglasNegocio.formato_fecha()))
    return nuevo_portafolio_dao.create(nuevoPortafolio)


def obteder_portafolio(idPortafolio):
    nuevo_portafolio_dao = portafolio_dao.Portafolio_Dao()
    return nuevo_portafolio_dao.get(idPortafolio)


def actualizar_saldo_portafolio(portafolio):
    nuevo_portafolio_dao = portafolio_dao.Portafolio_Dao()
    return nuevo_portafolio_dao.update(portafolio.get_id_portafolio(), portafolio.get_saldo_actual())
