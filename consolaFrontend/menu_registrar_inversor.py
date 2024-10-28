from controllers import controllerTipoDocumento, controllerPortafolio,controllerTipoInversor, controllerRegistrarInversor, controllerInicioSesion, controllerUsuario
from consolaFrontend import menu_tipo_documento, menu_tipos
from negocio import portafolio, servicioReglasNegocio, usuario, inversor, tipoInversor
import validadorDato.ValidacionDatos


def solicitar_datos_inversor():
    while True:
        print(f"*******Registro Inversor*******")

        nuevo_tipo_inversor =  menu_tipo_inversor()
    
        nuevo_tipo_documento = menu_tipo_documento()
   
        cuit = menu_cuit()
    
        numero_documento = validadorDato.ValidacionDatos.extraccion_num_documento(cuit)
    
        email = menu_email()
   
        nombre = input(f'Ingrese su nombre: ')
   
        apellido = input(f'Ingrese su apellido: ')
    
        pasHas = menu_password()

        print("\n*******Verifique los datos ingresados*******")

        print(f"Tipo de Inversor: {nuevo_tipo_inversor.get_nombre()}")
        print(f"Tipo de Documento: {nuevo_tipo_documento.get_nombre()}")
        print(f"CUIT: {cuit}")
        print(f"Correo: {email}")
        print(f"Nombre: {nombre}")
        print(f"Apellido: {apellido}")
        print(f"Contraseña: {pasHas['password']}")

        if confirmar_datos():
                nuevo_usuario = usuario.Usuario(email, pasHas['password_has'], 2)
                #nuevo_portafolio = controllerPortafolio.crear_portafolio()
                nuevoInversor = inversor.Inversor(cuit, numero_documento, nombre, apellido, portafolio.Portafolio(None,0,servicioReglasNegocio.definir_fecha_actual(servicioReglasNegocio.formato_fecha())), nuevo_tipo_inversor, nuevo_tipo_documento, nuevo_usuario)
                return controllerRegistrarInversor.crear_inversor(nuevoInversor)
        else:
                print("\nIngrese los datos nuevamente.\n")


def confirmar_datos():
    while True:
        confirmacion = input("\n¿Son correctos? Por favor, ingrese 'S' para confirmar o 'N' para volver a ingresar los datos. ").strip().lower()
        if confirmacion == 's':
            return True
        elif confirmacion == 'n':
            return False
        else:
            print("Opción no válida. Por favor, ingrese 'S' para confirmar o 'N' para volver a ingresar los datos.")


def reingrese_dato(funcion, variable, texto):
    while not funcion(variable):
        variable = input(f"{texto} de nuevo: ")
    return variable

def menu_tipo_inversor():
    nuevo_tipo_inversor = controllerTipoInversor.cargar_menu_tipo_inversor()
    nuevo_tipo_inversor = validadorDato.ValidacionDatos.tipo_de_dato(controllerTipoInversor.cargar_menu_tipo_inversor,nuevo_tipo_inversor)
    return nuevo_tipo_inversor

def menu_tipo_documento():
    nuevo_tipo_documento = controllerTipoDocumento.cargar_menu_tipo_documento()
    nuevo_tipo_documento = validadorDato.ValidacionDatos.tipo_de_dato(controllerTipoDocumento.cargar_menu_tipo_documento,nuevo_tipo_documento)
    return nuevo_tipo_documento

def menu_cuit():
    cuit = input(f'Ingrese un CUIT: ')
    cuit = reingrese_dato(validadorDato.ValidacionDatos.valida_existencia_cuit_en_db,cuit,"El cuit ya existe o el formato no es válido, ingreselo ")
    return cuit

def menu_email():
    email = input(f'Ingrese un correo: ')
    email = reingrese_dato(validadorDato.ValidacionDatos.valida_existencia_mail_bd,email,"El correo ya existe o el formato no es válido, ingreselo ")
    return email

def menu_password():
    print('Ingrese una contraseña entre 8-16 dígitos que contenga algún carácter especial y números.')
    pas = input('Contraseña: ')  
    pas = reingrese_dato(validadorDato.ValidacionDatos.pw_es_valido, pas, "Ingrese una contraseña")
    pasHas = servicioReglasNegocio.crear_encriptacion_password(pas)
    return {'password': pas, 'password_has': pasHas} #pasHas

""" def menu_confirmar_datos(): """