class Inversor:
    
    def __init__(self, cuit, tipo_documento, numero_documento, nombre,  apellido, portafolio, tipo_inversor):
        self.cuit = cuit;
        self.__tipo_Documento = tipo_documento;
        self.__numero_documento = numero_documento;
        self.__nombre = nombre;
        self.__apellido = apellido;
        self.__portafolio = portafolio;
        self.__tipo_inversor = tipo_inversor;
        
    def get_numero_documento(self):
        return self.__numero_documento;
    
    def set_numero_documento(self, numero_documento):
        self.__numero_documento =numero_documento;
    
    def get_nombre(self):
        return self.__nombre;
    
    def set_nombre(self, nombre):
        self.__nombre =nombre;
        
    def get_apellido(self):
        return self.__apellido;
    
    def set_apellido(self, apellido):
        self.__apellido =apellido;
        
    def get_portafolio(self):
        return self.__portafolio;
    
    def set_portafolio(self, portafolio):
        self.__portafolio =portafolio;
    
    def get_tipo_inversor(self):
        return self.__tipo_inversor;
    
    def set_tipo_inversor(self, tipo_inversor):
        self.__tipo_inversor =tipo_inversor;
        
    def get_cuit(self):
        return self.__cuit;
    
    