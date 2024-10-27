from backend.clasesDAO import usuario_dao
from negocio import servicioReglasNegocio
from service import servicioEmail
from consolaFrontend import menu_recuperar_password

def recuperar_password(email):
    userDao = usuario_dao.Usuario_Dao()
    update_usuario = userDao.get(email)
    if update_usuario:
        password = modificar_pasword(update_usuario)
        return {
            "usuario": update_usuario,
            "password": password
        }
    else :
        return None

def modificar_pasword(usuario):
    nuevoPassword = servicioEmail.generar_contrasena() 
    pasHased = servicioReglasNegocio.crear_encriptacion_password(nuevoPassword)
    usuario.set_password(pasHased)
    userDao = usuario_dao.Usuario_Dao()
    userDao.update(usuario)
    return nuevoPassword
    

def recuperar_usuario(email):
    userDao = usuario_dao.Usuario_Dao()
    usuario = userDao.get(email)
    if usuario:
        return {"usuario": usuario}
    else:
        return None

def verificar_contraseña_actual(usuario, contraseña_ingresada):
    return servicioReglasNegocio.validar_password(contraseña_ingresada, usuario.get_password())

def actualizar_contraseña(usuario, nueva_contraseña_encriptada):
    userDao = usuario_dao.Usuario_Dao()
    usuario.set_password(nueva_contraseña_encriptada)
    userDao.update(usuario)