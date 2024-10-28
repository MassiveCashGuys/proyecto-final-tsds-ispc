class Accion:
    def __init__(self, id_accion, simbolo, nombre, cantidad, precio_venta_actual, cantidad_venta_diaria, fecha_apertura, minimo_diario, maximo_diario, ultimo_cierre, id_empresa):
        self.__id_accion = id_accion
        self.__simbolo = simbolo
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio_venta_actual = precio_venta_actual
        self.__cantidad_venta_diaria = cantidad_venta_diaria
        self.__fecha_apertura = fecha_apertura
        self.__minimo_diario = minimo_diario
        self.__maximo_diario = maximo_diario
        self.__ultimo_cierre = ultimo_cierre
        self.__id_empresa = id_empresa

    def get_id_accion(self):
        return self.__id_accion 

    def get_simbolo(self):
        return self.__simbolo

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio_venta_actual(self):
        return self.__precio_venta_actual

    def get_cantidad_venta_diaria(self):
        return self.__cantidad_venta_diaria

    def getFecha_apertura(self):
        return self.__fecha_apertura

    def get_minimo_diario(self):
        return self.__minimo_diario

    def get_maximo_diario(self):
        return self.__maximo_diario

    def get_ultimo_cierre(self):
        return self.__ultimo_cierre

    def get_id_empresa(self):
        return self.__id_empresa
    
    def set_simbolo(self, simbolo):
        self.__simbolo = simbolo
    
    def set_nombre(self, nombre):
        self.__nombre = nombre      
    
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad      

    def set_precio_venta_actual(self, precio_venta_actual):
        self.__precio_venta_actual = precio_venta_actual

    def set_cantidad_venta_diaria(self, cantidad_venta_diaria):
        self.__cantidad_venta_diaria = cantidad_venta_diaria    

    def setFecha_apertura(self, fecha_apertura):    
        self.__fecha_apertura = fecha_apertura    

    def set_minimo_diario(self, minimo_diario): 
        self.__minimo_diario = minimo_diario    

    def set_maximo_diario(self, maximo_diario): 
        self.__maximo_diario = maximo_diario    

    def set_ultimo_cierre(self, ultimo_cierre): 
        self.__ultimo_cierre = ultimo_cierre    

    def set_id_empresa(self, id_empresa):
        self.__id_empresa = id_empresa  
    


