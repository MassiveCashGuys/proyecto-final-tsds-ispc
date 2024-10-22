from controllers import controllerTipoDocumento, controllerPortafolio,controllerTipoInversor, controllerRegistrarInversor, controllerInicioSesion
from consolaFrontend import menu_tipo_documento, menu_tipos
from negocio import servicioReglasNegocio, usuario, inversor, tipoInversor
import validadorDato.ValidacionDatos



def solicitar_datos_inversor():
    print(f"********Registro Inversor********")

    #user = usuario.Usuario("hahahat@gmail.com", servicioReglasNegocio.crear_encriptacion_password("pepito"),1)
    #print(user)
    #print(controllerInicioSesion.crear_usuario(user))
    nuevo_tipo_inversor = controllerTipoInversor.cargar_menu_tipo_inversor()
    nuevo_tipo_inversor = validadorDato.ValidacionDatos.tipo_de_dato(controllerTipoInversor.cargar_menu_tipo_inversor,nuevo_tipo_inversor)
    nuevo_tipo_documento = controllerTipoDocumento.cargar_menu_tipo_documento()
    nuevo_tipo_documento = validadorDato.ValidacionDatos.tipo_de_dato(controllerTipoDocumento.cargar_menu_tipo_documento,nuevo_tipo_documento)
    #numero_documento = input(f'Ingrese un número de documento: ')
    cuit = input(f'Ingrese un CUIT: ')
    cuit = reingrese_dato(validadorDato.ValidacionDatos.cuit_es_valido,cuit,"Ingrese un CUIT")
    numero_documento = validadorDato.ValidacionDatos.extraccion_num_documento(cuit)
    email = input(f'Ingrese un correo: ')
    email=reingrese_dato(validadorDato.ValidacionDatos.validar_formato_email,email,"Ingrese un correo")
    nombre= input(f'Ingrese su nombre: ')
    apellido = input(f'Ingrese su apellido: ')
    print(f'Ingrese una contraseña entre 8-16 digitos que contenga algún caracter especial y números.')
    pas = input(f'Contraseña: ')
    reingrese_dato(validadorDato.ValidacionDatos.pw_es_valido,pas,"Ingrese una contraseña")


def reingrese_dato(funcion, variable, texto):

    while True:
        if funcion(variable):
            return variable
        else:
            variable = input(f"{texto} de nuevo: ")
    

