from controllers import controllerTipoDocumento, controllerRegistrarInversor
from consolaFrontend import menu_tipo_documento
import validadorDato.ValidacionDatos

def solicitar_datos_inversor():
    print(f"********Registro Inversor********")
    controllerTipoDocumento.cargar_menu_tipo_documento()
    cuit = input(f'Ingrese un CUIT: ')
    reingrese_dato(validadorDato.ValidacionDatos.cuit_es_valido,cuit,"Ingrese un CUIT")
    email = input(f'Ingrese un correo: ')
    reingrese_dato(validadorDato.ValidacionDatos.validar_formato_email,email,"Ingrese un correo")
    nombre= input(f'Ingrese su nombre: ')
    apellido = input(f'Ingrese su apellido: ')
    pas = input(f'Ingrese una contraseña: ')
    reingrese_dato(validadorDato.ValidacionDatos.pw_es_valido,pas,"Ingrese una contraseña")
    

def reingrese_dato(funcion, variable, texto):

    while True:
        if funcion(variable):
            break
        else:
            variable = input(f"{texto} de nuevo: ")


