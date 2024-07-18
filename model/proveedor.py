class Proveedor:
    def __init__(self, id_proveedor, denominacion, telefono, email):
        self.id_proveedor = id_proveedor
        self.denominacion = denominacion
        self.telefono = telefono
        self.email = email

    def set_id_proveedor(self, id_proveedor):
        self.__id_proveedor = id_proveedor
    
    def set_denominacion(self, denominacion):
        self.__denominacion = denominacion

    def set_telefono(self, telefono):
        self.__telefono = telefono
    
    def set_email(self, email):
        self.__email = email



    def set_id_proveedor(self):
        return self.__id_proveedor 
    
    def set_denominacion(self):
        return self.__denominacion

    def set_telefono(self):
        return self.__telefono
    
    def set_email(self):
        return self.__email

