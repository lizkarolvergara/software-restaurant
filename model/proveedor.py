class Proveedor:
    def __init__(self, id_proveedor, nombre, contacto, telefono):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.contacto = contacto
        self.telefono = telefono

    def set_id_proveedor(self, id_proveedor):
        self.__id_proveedor = id_proveedor
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_contacto(self, contacto):
        self.__contacto = contacto

    def set_telefono(self, telefono):
        self.__telefono = telefono
    


    def set_id_proveedor(self):
        return self.__id_proveedor 
    
    def set_nombre(self):
        return self.__nombre

    def set_contacto(self):
        return self.__contacto

    def set_telefono(self):
        return self.__telefono

