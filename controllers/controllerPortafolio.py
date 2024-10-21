from backend.clasesDAO import portafolio_dao
from negocio import portafolio, servicioReglasNegocio


def cargar_saldo_inicial(id_portafolio):
    aux = portafolio_dao.Portafolio_Dao()
    aux.update(saldo=1000000, portafolio=id_portafolio)

def crear_portafolio()->portafolio.Portafolio:
    nuevo_portafolio_dao = portafolio_dao.Portafolio_Dao()
    nuevoPortafolio= portafolio.Portafolio(None,0, servicioReglasNegocio.definir_fecha_actual())
    return nuevo_portafolio_dao.create(nuevoPortafolio)
    