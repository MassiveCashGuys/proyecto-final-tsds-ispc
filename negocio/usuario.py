# crear atributos y metodos para la clase usuario
# clase usuario

class Usuario: 
    def __init__(self, id_user, password, id_perfil):# cambiar contraseña por password 
        
        self.__id_user = id_user
        self.__password = password
        self.__id_perfil = id_perfil

    def get_id_user(self):
        return self.__id_user
    
    def get_password(self):
        return self.__password
    
    def get_id_perfil(self):
        return self.__id_perfil    

# id no tiene set pq no lo podemos modificar.

    def set_password(self, password):
        self.__password = password

    def set_id_perfil(self, id_perfil):
        self.__id_perfil = id_perfil

    def __str__(self) -> str:
        return f"id_user: {self.__id_user}, password: {self.__password}, id_perfil: {self.__id_perfil}"