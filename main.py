from controllers import controllerInicioSesion
from negocio import servicioReglasNegocio


def main():
<<<<<<< HEAD
    pas = servicioReglasNegocio.crear_encriptacion_password("Pepito")
    print(pas)
    print(servicioReglasNegocio.validar_password(pas, "Pepito"))
    controllerInicioSesion.inicio_sesion()

    # Carga de saldo inicial y muestra de mensaje
    print(servicioReglasNegocio.asignar_saldo_inicial(idporfolio=1))

=======
   controllerInicioSesion.inicio_sesion()
   
>>>>>>> origin/back

if __name__ == "__main__":
    main()
