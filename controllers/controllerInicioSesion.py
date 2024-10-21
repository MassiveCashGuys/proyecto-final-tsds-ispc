from consolaFrontend import login
from backend.clasesDAO import usuario_dao

def inicio_sesion():
    login.mostar_menu_inicio_sesion()

def crear_usuario(user):
    user_dao = usuario_dao.Usuario_Dao()
    flag = user_dao.create(user)
    return flag
