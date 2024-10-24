
from backend.clasesDAO import detalle_portafolio_dao


def crear_detalle_portafolio(detallePortafolio):
    detallePortafolioDao = detalle_portafolio_dao.Detalle_Portafolio_Dao()
    return detallePortafolioDao.create(detallePortafolio)