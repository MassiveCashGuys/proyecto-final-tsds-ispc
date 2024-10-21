from consolaFrontend import menu_tipo_documento
from consolaFrontend import menu_registrar_inversor
from backend.clasesDAO import usuario_dao, inversor_dao
from controllers import controllerPortafolio

def cargar_menu_tipo_documento():
    menu_tipo_documento.menu_tipo_documento()

def cargar_menu_registro_inversor():
    menu_registrar_inversor.solicitar_datos_inversor()


def crear_inversor(inversor):
    
    userDao = usuario_dao.Usuario_Dao();
    userDao.create(inversor.get_user())
    inversorDao = inversor_dao.InversorDao()
    updateInversor= inversorDao.create(inversor)
    updatePortafolio = controllerPortafolio.obteder_portafolio(updateInversor.get_portafolio())
    updateInversor.set_portafolio(updatePortafolio)
    cargar_saldo_inicial(updateInversor)

def cargar_saldo_inicial(inversor):
    controllerPortafolio.cargar_saldo_inicial(inversor.get_portafolio().get_id_portafolio())
      

