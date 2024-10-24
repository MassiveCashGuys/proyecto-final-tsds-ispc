from backend.clasesDAO import accion_dao
def obtener_acciones():
    accionDao = accion_dao.AccionDao()
    return  accionDao.getAll()

def actualizar_accion(accion):
    accionDao = accion_dao.AccionDao()
    return accionDao.update(accion)