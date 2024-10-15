from controllers import controllerTipoDocumento
from consolaFrontend import menu_tipo_documento

def solicitar_datos_inversor():
    print(f"********Registro Inversor********")
    cuit = input(f'Ingrese un CUIT')
    menu_tipo_documento.menu_tipo_documento()
    email = input(f'Ingrese un correo')
    nombre= input(f'Ingrese su nombre')
    apellido = input(f'Ingrese su apellido')
    pas = input(f'Ingrese una contraseña')
    
    
    
    
    