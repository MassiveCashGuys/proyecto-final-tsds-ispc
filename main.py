from backend.clasesDAO import tipo_documento_dao
import consolaFrontend.menuPrincipal
from negocio import tipoDocumento
from consolaFrontend import menuPrincipal

def main():
   """  tipoDocumentoDao=tipo_documento_dao.Tipo_Documento_Dao()
    doc= tipoDocumento.TipoDocumento(1,"LC","Libreta Cívica")
    tipoDocumentoDao.update(doc) """
   menuPrincipal.mostrar_menu_principal(6)
   
if __name__ == "__main__":
    main()