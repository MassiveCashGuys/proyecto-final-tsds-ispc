
class TipoInversor:
    # Tipos de documentos
    # DNI = Documento Nacional de Identidad 
    # LE = Libreta de Enrolamiento
    # LC = Libreta Cívica
    # PASAPORTE = Pasaporte
    # CI = Cédula de Identidad

    def __init__(self, id_tipo_inversor, nombre, descripcion):
        self.__id_tipo_inversor = id_tipo_inversor
        self.__nombre = nombre
        self.__descripcion = descripcion

    def get_id_id_tipo_inversor(self):
        return self.__id_tipo_inversor

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_descripcion(self):
        return self.__descripcion

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion
