from backend.clasesDAO import tipo_inversor_dao
from consolaFrontend import menu_tipos
from controllers import controllerTipoInversor

def obtener_lista_tipo()->list:
   dao_tipo_inversor = tipo_inversor_dao.Tipo_Inversor_Dao()
   return dao_tipo_inversor.getAll()

def cargar_menu_tipo_inversor():
    """ titulo, moduloController, ingresoDato """
    titulo = "Tipo de Inversor"
    ingresoDato = " ingrese solo el nombre"
    return menu_tipos.mostar_menu_tipo(titulo,controllerTipoInversor, ingresoDato)