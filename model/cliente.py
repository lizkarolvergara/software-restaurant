class Cliente:
    def __init__(self, id_cliente, denominacion, telefono):
        self.id_cliente = id_cliente
        self.denominacion = denominacion
        self.telefono = telefono
    
    def set_id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente
    
    def set_denominacion(self, denominacion):
        self.__denominacion = denominacion

    def set_telefono(self,telefono):
        self.__telefono = telefono
    


    def set_id_cliente(self):
        return self.__id_cliente
    
    def set_denominacion(self):
        return self.__denominacion
    
    def set_telefono(self):
        return self.__telefono
 

