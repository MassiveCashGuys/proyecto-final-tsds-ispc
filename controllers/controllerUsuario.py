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
    nuevoPassword =servicioEmail.generar_contrasena() 
    pasHased = servicioReglasNegocio.crear_encriptacion_password(nuevoPassword)
    usuario.set_password(pasHased)
    userDao = usuario_dao.Usuario_Dao()
    userDao.update(usuario)
    return nuevoPassword
    
    