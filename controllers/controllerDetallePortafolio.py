# from backend.clasesDAO import accion_dao
from backend.clasesDAO import detalle_portafolio_dao


def crear_detalle_portafolio(detallePortafolio):
    detallePortafolioDao = detalle_portafolio_dao.Detalle_Portafolio_Dao()
    return detallePortafolioDao.create(detallePortafolio)


def obtener_acciones_portafolio(fk):
    # accionDao = accion_dao.AccionDao()
    detallePortafolioDao = detalle_portafolio_dao.Detalle_Portafolio_Dao()
    # return accionDao.getAll()
    return detallePortafolioDao.get_by_fk(fk)
