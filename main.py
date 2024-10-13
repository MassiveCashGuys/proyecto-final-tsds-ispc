from backend.clasesDAO import tipo_documento_dao
from negocio import tipoDocumento

def main():
    tipoDocumentoDao=tipo_documento_dao.Tipo_Documento_Dao()
    doc= tipoDocumento.TipoDocumento(1,"LC","Libreta Cívica")
    tipoDocumentoDao.update(doc)
   
if __name__ == "__main__":
    main()