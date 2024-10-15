from backend.clasesDAO import tipo_documento_dao

def obtener_lista_tipo_documento()->list:
    dao_tipo_documento = tipo_documento_dao.Tipo_Documento_Dao()
    return dao_tipo_documento.getAll()