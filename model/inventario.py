class Inventario:
    def __init__(self, id_inventario, id_plato, cantidaddisponible, puntodereorden):
        self.id_inventario = id_inventario
        self.id_plato = id_plato
        self.cantidaddisponible = cantidaddisponible
        self.puntodereorden = puntodereorden

    def set_id_inventario(self, id_inventario):
        self.__id_inventario = id_inventario
    
    def set_id_plato(self, id_plato):
        self.__id_plato = id_plato

    def set_cantidaddisponible(self, cantidaddisponible):
        self.__cantidaddisponible = cantidaddisponible

    def set_puntodereorden(self, puntodereorden):
        self.__puntodereorden = puntodereorden

    


    def set_id_inventario(self):
        return self.__id_inventario 
    
    def set_id_plato(self):
        return self.__id_plato

    def set_cantidaddisponible(self):
        return self.__cantidaddisponible

    def set_puntodereorden(self):
        return self.__puntodereorden

