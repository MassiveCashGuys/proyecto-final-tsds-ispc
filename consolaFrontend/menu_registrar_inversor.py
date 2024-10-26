from controllers import controllerTipoDocumento, controllerPortafolio,controllerTipoInversor, controllerRegistrarInversor, controllerInicioSesion, controllerUsuario
from consolaFrontend import menu_tipo_documento, menu_tipos
from negocio import servicioReglasNegocio, usuario, inversor, tipoInversor
import validadorDato.ValidacionDatos



def solicitar_datos_inversor():
    while True:
        print(f"*******Registro Inversor*******")

        nuevo_tipo_inversor = controllerTipoInversor.cargar_menu_tipo_inversor()
        nuevo_tipo_inversor = validadorDato.ValidacionDatos.tipo_de_dato(controllerTipoInversor.cargar_menu_tipo_inversor, nuevo_tipo_inversor)
 
        nuevo_tipo_documento = controllerTipoDocumento.cargar_menu_tipo_documento()
        nuevo_tipo_documento = validadorDato.ValidacionDatos.tipo_de_dato(controllerTipoDocumento.cargar_menu_tipo_documento, nuevo_tipo_documento)
       
        cuit = input('Ingrese un CUIT: ')
        cuit = reingrese_dato(validadorDato.ValidacionDatos.valida_existencia_cuit_en_db, cuit, "El CUIT ya existe o el formato no es válido, ingréselo")
        
        numero_documento = validadorDato.ValidacionDatos.extraccion_num_documento(cuit)
        
        email = input('Ingrese un correo: ')
        email = reingrese_dato(validadorDato.ValidacionDatos.valida_existencia_mail_bd, email, "El correo ya existe o el formato no es válido, ingréselo")
       
        nombre = input('Ingrese su nombre: ')
       
        apellido = input('Ingrese su apellido: ')

        print('Ingrese una contraseña entre 8-16 dígitos que contenga algún carácter especial y números.')
        pas = input('Contraseña: ')
        
        pas = reingrese_dato(validadorDato.ValidacionDatos.pw_es_valido, pas, "Ingrese una contraseña")
        pasHas = servicioReglasNegocio.crear_encriptacion_password(pas)

        print("\n*******Verifique los datos ingresados*******")

        print(f"Tipo de Inversor: {nuevo_tipo_inversor.get_nombre()}")
        print(f"Tipo de Documento: {nuevo_tipo_documento.get_nombre()}")
        print(f"CUIT: {cuit}")
        print(f"Correo: {email}")
        print(f"Nombre: {nombre}")
        print(f"Apellido: {apellido}")
        print(f"Contraseña: {pas}")  


        while True:
            confirmacion = input("\n¿Son correctos? Por favor, ingrese 'S' para confirmar o 'N' para volver a ingresar los datos. ").strip().lower()
            if confirmacion == 's':
                nuevo_usuario = usuario.Usuario(email, pasHas, 2)
                nuevo_portafolio = controllerPortafolio.crear_portafolio()
                nuevoInversor = inversor.Inversor(cuit, numero_documento, nombre, apellido, nuevo_portafolio, nuevo_tipo_inversor, nuevo_tipo_documento, nuevo_usuario)
                return controllerRegistrarInversor.crear_inversor(nuevoInversor)
            elif confirmacion == 'n':
                print("\nIngrese los datos nuevamente.\n")
                break  
            else:
                print("Opción no válida. Por favor, ingrese 'S' para confirmar o 'N' para volver a ingresar los datos.")

def reingrese_dato(funcion, variable, texto):
    while not funcion(variable):
        variable = input(f"{texto} de nuevo: ")
    return variable
