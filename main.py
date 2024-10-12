from backend.clasesDAO import tipo_documento_dao
from negocio import tipoDocumento
def main():
    tipoDocumentoDao=tipo_documento_dao.Tipo_Documento_Dao()
    tipo_documento = tipoDocumento.TipoDocumento(None, "LC" , "Libreta Cívica")
    tipoDocumentoDao.create(tipo_documento);
    print(tipo_documento.get_nombre());

if __name__ == "__main__":
    main()