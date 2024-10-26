from controllers import controllerTipoDocumento, controllerPortafolio,controllerTipoInversor, controllerRegistrarInversor, controllerInicioSesion, controllerUsuario
from consolaFrontend import menu_tipo_documento, menu_tipos
from negocio import servicioReglasNegocio, usuario, inversor, tipoInversor
import validadorDato.ValidacionDatos



def solicitar_datos_inversor():
    print(f"********Registro Inversor********")

    nuevo_tipo_inversor = controllerTipoInversor.cargar_menu_tipo_inversor()
    nuevo_tipo_inversor = validadorDato.ValidacionDatos.tipo_de_dato(controllerTipoInversor.cargar_menu_tipo_inversor,nuevo_tipo_inversor)
   
    nuevo_tipo_documento = controllerTipoDocumento.cargar_menu_tipo_documento()
    nuevo_tipo_documento = validadorDato.ValidacionDatos.tipo_de_dato(controllerTipoDocumento.cargar_menu_tipo_documento,nuevo_tipo_documento)
   
    cuit = input(f'Ingrese un CUIT: ')
    cuit = reingrese_dato(validadorDato.ValidacionDatos.valida_existencia_cuit_en_db,cuit,"El cuit ya existe o el formato no es válido, ingreselo ")
    
    numero_documento = validadorDato.ValidacionDatos.extraccion_num_documento(cuit)
    
    email = input(f'Ingrese un correo: ')
    email = reingrese_dato(validadorDato.ValidacionDatos.valida_existencia_mail_bd,email,"El correo ya existe o el formato no es válido, ingreselo ")
   
    nombre = input(f'Ingrese su nombre: ')
   
    apellido = input(f'Ingrese su apellido: ')
    print(f'Ingrese una contraseña entre 8-16 digitos que contenga algún caracter especial y números.')
    pas = input(f'Contraseña: ')

    #confirmación de datos son correctos
    
    pas= reingrese_dato(validadorDato.ValidacionDatos.pw_es_valido,pas,"Ingrese una contraseña")
    pasHas= servicioReglasNegocio.crear_encriptacion_password(pas)
    nuevo_usuario = usuario.Usuario(email, pasHas, 2)
    nuevo_portafolio = controllerPortafolio.crear_portafolio()
    nuevoInversor = inversor.Inversor(cuit, numero_documento, nombre, apellido, nuevo_portafolio, nuevo_tipo_inversor, nuevo_tipo_documento, nuevo_usuario)
    return controllerRegistrarInversor.crear_inversor(nuevoInversor)
    

def reingrese_dato(funcion, variable, texto):

    while True:
        if funcion(variable):
            return variable
        else:
            variable = input(f"{texto} de nuevo: ")
    

