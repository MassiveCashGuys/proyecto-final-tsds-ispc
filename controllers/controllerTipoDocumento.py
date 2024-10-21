from backend.clasesDAO import tipo_documento_dao
from consolaFrontend import menu_tipos
from controllers import controllerTipoDocumento

def obtener_lista_tipo()->list:
   dao_tipo_documento = tipo_documento_dao.Tipo_Documento_Dao()
   return  dao_tipo_documento.getAll()

def cargar_menu_tipo_documento():
    """ titulo, moduloController, ingresoDato """
    titulo = "Tipo de Documentos"
    ingresoDato = " ingrese solo las iniciales"
    return menu_tipos.mostar_menu_tipo(titulo,controllerTipoDocumento, ingresoDato)