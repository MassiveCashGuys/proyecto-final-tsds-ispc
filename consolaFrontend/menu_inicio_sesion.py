# Gustavo 
# Tarea 14 y 16
from backend.clasesDAO.usuario_dao import Usuario_Dao
from negocio import servicioReglasNegocio


def menu_inicio_login():

    print("\n")
    print(f"******************************")
    print(f"**     INICIO DE SESIÓN     **")
    print(f"******************************")
    print("\n")
    email = input(f'Ingrese su correo: ')
    password = servicioReglasNegocio.input_con_asteriscos(f'Ingrese su contraseña: ')



    # Verifica si el email existe en la base de datos
    usuario_dao = Usuario_Dao()
    user = usuario_dao.get(email)

    if user:        

        # Verifica si la contraseña es correcta
        if servicioReglasNegocio.validar_password(password, user.get_password()):
            print("\n")
            print(" ✅ Ingreso correcto ✅")
            print("\n")
            print("Bienvenido " + user.get_id_user() + " 🙋‍♂️ 🙋‍♀️") # Cambiar para que agregue el nombre desde inventario.
            print("\n")            
            return user
        else:
            print("\n")
            print("Error: Email o Contraseña incorrecta ⚠️ ")
            print("\n")
            return None
    else:
        print("\n")
        print("Error: Email o Contraseña incorrecta ⚠️ ")
        print("\n")
        return None