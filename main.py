from controllers import controllerInicioSesion
# from negocio import servicioReglasNegocio


def main():
    # Carga de saldo inicial y muestra de mensaje
    # print(servicioReglasNegocio.asignar_saldo_inicial(idporfolio=1))
    controllerInicioSesion.inicio_sesion()


if __name__ == "__main__":
    main()