from backend.clasesDAO import portafolio_dao


def cargar_saldo_inicial(id_portafolio):
    aux = portafolio_dao.Portafolio_Dao()
    aux.update(saldo=1000000, portafolio=id_portafolio)
