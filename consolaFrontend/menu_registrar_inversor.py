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
    print(f'Ingrese una contraseña entre 8-16 digitos que contenga algún caracter especial y números.')
    pas = input(f'Contraseña: ')
    reingrese_dato(validadorDato.ValidacionDatos.pw_es_valido,pas,"Ingrese una contraseña")
    # Confirmación de datos
    print(f"¿Los datos ingresados son correctos? Presione Y para continuar, N para volver a ingresar sus datos")
    print(f"Su CUIT: ", cuit)
    print(f"Su correo: ", email)
    print(f"Su nombre: ", nombre)
    print(f"Su apellido: ", apellido)

    while True:
        respuesta = input("Ingrese su respuesta (Y/N): ").strip().lower()
        if respuesta == 'y':
            guardar_datos(cuit, email, nombre, apellido, pas)
            break
        elif respuesta == 'n':
            print("Por favor, vuelva a ingresar la información.\n")
            return
        else:
            print("Respuesta no válida. Por favor, ingrese 'Y' para sí o 'N' para no.")

def reingrese_dato(funcion, variable, texto):

    while True:
        if funcion(variable):
            break
        else:
            variable = input(f"{texto} de nuevo: ")


def guardar_datos(cuit, email, nombre, apellido, pas):
    print("Datos guardados correctamente.")