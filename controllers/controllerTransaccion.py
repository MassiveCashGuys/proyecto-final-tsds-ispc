from backend.clasesDAO import transaccion_dao


def crear_transaccion(transaccion):
    transaccionDao = transaccion_dao.Transaccion_Dao()
    return transaccionDao.create(transaccion)


def listar_transacciones(inversor):
    transaccionDao = transaccion_dao.Transaccion_Dao()
    transacciones_x_inversor = transaccionDao.get_by_fk(inversor)

    for x in transacciones_x_inversor:
        print(x)
        print("\n")
