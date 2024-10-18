from consolaFrontend import login
from backend.clasesDAO import usuario_dao
from negocio import servicioReglasNegocio

def inicio_sesion():
    login.mostar_menu_inicio_sesion()

def crear_usuario(user):
    user_dao = usuario_dao.Usuario_Dao()
    flag = user_dao.create(user)
    return flag

def obtener_usuario(email):
    user_dao = usuario_dao.Usuario_Dao()
    user = user_dao.get(email)
    return user

def validar_password(user, password):
    print(user.get_password())
    flag = servicioReglasNegocio.validar_password(user.get_password().encode('utf-8'), password)
    return flag
