from controllers import controllerTipoDocumento, controllerPortafolio, controllerTipoInversor, controllerRegistrarInversor, controllerInicioSesion, controllerUsuario
from consolaFrontend import menu_tipo_documento, menu_tipos
from negocio import servicioReglasNegocio, usuario, inversor, tipoInversor
import validadorDato.ValidacionDatos


def solicitar_datos_inversor():
    while True:
        print(f"*******Registro Inversor*******")

    # user = usuario.Usuario("hahahat@gmail.com", servicioReglasNegocio.crear_encriptacion_password("pepito"),1)
    # print(user)
    # print(controllerInicioSesion.crear_usuario(user))
    nuevo_tipo_inversor = controllerTipoInversor.cargar_menu_tipo_inversor()
    numero_documento = input(f'Ingrese un número de documento: ')
    nuevo_tipo_documento = controllerTipoDocumento.cargar_menu_tipo_documento()
    cuit = input(f'Ingrese un CUIT: ')
    cuit = reingrese_dato(
        validadorDato.ValidacionDatos.cuit_es_valido, cuit, "Ingrese un CUIT")
    email = input(f'Ingrese un correo: ')
    email = reingrese_dato(
        validadorDato.ValidacionDatos.validar_formato_email, email, "Ingrese un correo")
    nombre = input(f'Ingrese su nombre: ')
    apellido = input(f'Ingrese su apellido: ')
    print(f'Ingrese una contraseña entre 8-16 digitos que contenga algún caracter especial y números.')
    pas = input(f'Contraseña: ')
    pas = reingrese_dato(
        validadorDato.ValidacionDatos.pw_es_valido, pas, "Ingrese una contraseña")
    pasHas = servicioReglasNegocio.crear_encriptacion_password(pas)
    nuevo_usuario = usuario.Usuario(email, pasHas, 1)
    nuevo_portafolio = controllerPortafolio.crear_portafolio()
    nuevoInversor = inversor.Inversor(cuit, numero_documento, nombre, apellido,
                                      nuevo_portafolio, nuevo_tipo_inversor, nuevo_tipo_documento, nuevo_usuario)
    return controllerRegistrarInversor.crear_inversor(nuevoInversor)


def reingrese_dato(funcion, variable, texto):

    while True:
        if funcion(variable):
            return variable
        else:
            variable = input(f"{texto} de nuevo: ")
