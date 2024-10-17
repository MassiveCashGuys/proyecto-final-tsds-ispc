from controllers import controllerTipoDocumento, controllerRegistrarInversor, controllerInicioSesion
from consolaFrontend import menu_tipo_documento
from negocio import servicioReglasNegocio, usuario
import validadorDato.ValidacionDatos



def solicitar_datos_inversor():
    print(f"********Registro Inversor********")

    #user = usuario.Usuario("hahahat@gmail.com", servicioReglasNegocio.crear_encriptacion_password("pepito"),1)
    #print(user)
    #print(controllerInicioSesion.crear_usuario(user))
    
    controllerTipoDocumento.cargar_menu_tipo_documento()
    cuit = input(f'Ingrese un CUIT: ')
    reingrese_dato(validadorDato.ValidacionDatos.cuit_es_valido,cuit,"Ingrese un CUIT")
    email = input(f'Ingrese un correo: ')
    reingrese_dato(validadorDato.ValidacionDatos.validar_formato_email,email,"Ingrese un correo")
    nombre= input(f'Ingrese su nombre: ')
    apellido = input(f'Ingrese su apellido: ')
    print(f'Ingrese una contraseña entre 8-16 digitos que contenga algún caracter especial y números.')
    pas = input(f'Contraseña: ')
    reingrese_dato(validadorDato.ValidacionDatos.pw_es_valido,pas,"Ingrese una contraseña")
    

def reingrese_dato(funcion, variable, texto):

    while True:
        if funcion(variable):
            break
        else:
            variable = input(f"{texto} de nuevo: ")


