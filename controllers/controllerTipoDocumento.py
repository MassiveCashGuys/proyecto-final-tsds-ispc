from backend.clasesDAO import tipo_documento_dao
from consolaFrontend import menu_tipo_documento

def obtener_lista_tipo_documento()->list:
    dao_tipo_documento = tipo_documento_dao.Tipo_Documento_Dao()
    return dao_tipo_documento.getAll()

def cargar_menu_tipo_documento():
    menu_tipo_documento.mostar_menu_tipo_documento()