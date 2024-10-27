from backend.clasesDAO import usuario_dao
from negocio import servicioReglasNegocio
from service import servicioEmail


def recuperar_password(email):
    userDao = usuario_dao.Usuario_Dao()
    update_usuario = userDao.get(email)
    if update_usuario:
        password = modificar_pasword(update_usuario, None)
        return {
            "usuario": update_usuario,
            "password": password
        }
    else :
        return None

def modificar_pasword(usuario,nuevoPassword):
    if nuevoPassword: 
        pasHased = servicioReglasNegocio.crear_encriptacion_password(nuevoPassword)
    else:
        nuevoPassword =servicioEmail.generar_contrasena() 
        pasHased = servicioReglasNegocio.crear_encriptacion_password(nuevoPassword)
    usuario.set_password(pasHased)
    userDao = usuario_dao.Usuario_Dao()
    userDao.update(usuario)
    return nuevoPassword


def verificar_contraseña_actual(usuario, contraseña_ingresada):
    return servicioReglasNegocio.validar_password(contraseña_ingresada, usuario.get_password())


def recuperar_usuario(email):
    userDao = usuario_dao.Usuario_Dao()
    return userDao.get(email)


