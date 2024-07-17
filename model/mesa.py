class Mesa:
    def __init__(self, id_mesa, numero, estado):
        self.id_mesa = id_mesa
        self.numero = numero
        self.estado = estado

    def set_id_mesa(self, id_mesa):
        self.__id_mesa = id_mesa
    
    def set_numero(self, numero):
        self.__numero = numero

    def set_apellido(self, estado):
        self.__estado = estado

    

    def set_id_mesa(self):
        return self.__id_mesa
    
    def set_numero(self):
        return self.__numero

    def set_apellido(self):
        return self.__estado 


