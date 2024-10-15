from controllers import controllerInicioSesion
from negocio import servicioReglasNegocio

def main():
   pas = servicioReglasNegocio.crear_encriptacion_password("Pepito")
   print(pas)
   print(servicioReglasNegocio.validar_password(pas,"Pepito"))
   controllerInicioSesion.inicio_sesion()
   
   
   
if __name__ == "__main__":
    main()