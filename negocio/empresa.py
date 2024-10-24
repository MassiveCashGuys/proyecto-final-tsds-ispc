class Empresa:
    
    def __init__(self, id_empresa, nombre, rason_social, descripcion):
        self.__id_empresa = id_empresa
        self.__nombre = nombre
        self.__rason_social = rason_social
        self.__descripcion = descripcion

    def get_id_empresa(self):
        return self.__id_empresa

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_rason_social(self):
        return self.__rason_social

    def set_rason_social(self, rason_social):
        self.__rason_social = rason_social

    def get_descripcion(self):
        return self.__descripcion

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion
    
    def set_rason_social(self, rason_social):
        self.__rason_social = rason_social
        
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def __str__(self):
        return f"{self.__id_empresa}, {self.__nombre}, {self.__rason_social}, {self.__descripcion}"
