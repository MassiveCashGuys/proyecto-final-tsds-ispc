from backend.clasesDAO import tipo_documento_dao
import consolaFrontend.menuPrincipal
from negocio import tipoDocumento, servicioReglasNegocio
from consolaFrontend import menuPrincipal
from validadorDato import validador

def main():
   """  tipoDocumentoDao=tipo_documento_dao.Tipo_Documento_Dao()
    doc= tipoDocumento.TipoDocumento(1,"LC","Libreta Cívica")
    tipoDocumentoDao.update(doc) """
   """ menuPrincipal.mostrar_menu_principal(6) """
   print(validador.is_number(6))
   print(validador.is_number(6.5))
   print(validador.is_number("6.5p"))
   print(validador.is_number("6a0"))
   pas = servicioReglasNegocio.crear_encriptacion_password("julio428")
   print(servicioReglasNegocio.validar_password(pas,"julio428")) 
   
   
   
if __name__ == "__main__":
    main()