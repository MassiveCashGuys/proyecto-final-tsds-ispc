from backend.clasesDAO import inversor_dao
def obtener_inversor(user):
    inversorDao = inversor_dao.InversorDao()
    return inversorDao.get_by_fk(user.get_id_user())