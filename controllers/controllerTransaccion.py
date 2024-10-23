from backend.clasesDAO import transaccion_dao
def crear_transaccion(transaccion):
   transaccionDao = transaccion_dao.Transaccion_Dao()
   return transaccionDao.create(transaccion)