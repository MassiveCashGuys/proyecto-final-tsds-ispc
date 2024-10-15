from controllers import controllerInicioSesion
from negocio import servicioReglasNegocio
from negocio import servicioReglasNegocio


def main():
    print(servicioReglasNegocio.asignar_saldo_inicial(idporfolio=1))


if __name__ == "__main__":
    main()
