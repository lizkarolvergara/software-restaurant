class Plato:
    def __init__(self, id_plato, nombre, descripcion, precio, disponibilidad):
        self.id_plato = id_plato
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.disponibilidad = disponibilidad

    def set_id_plato(self, id_plato):
        self.__id_plato = id_plato
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def set_precio(self, precio):
        self.__precio = precio

    def set_disponibilidad(self, disponibilidad):
        self.__disponibilidad = disponibilidad


    

    def set_id_plato(self):
        return self.__id_plato
    
    def set_nombre(self):
        return self.__nombre

    def set_descripcion(self):
        return self.__descripcion

    def set_precio(self):
        return self.__precio

    def set_disponibilidad(self):
        return self.__disponibilidad 