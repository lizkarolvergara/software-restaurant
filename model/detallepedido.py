class DetallePedido:
    def __init__(self, id_detallepedido, id_pedido, id_plato, unitario, total):
        self.id_detallepedido = id_detallepedido
        self.id_pedido = id_pedido
        self.id_plato = id_plato
        self.unitario = unitario
        self.total = total
    
    def set_id_detallepedido(self, id_detallepedido):
        self.__id_detallepedido = id_detallepedido
    
    def set_id_pedido(self, id_pedido):
        self.__id_pedido = id_pedido

    def set_id_plato(self, id_plato):
        self.__id_plato = id_plato

    def set_unitario(self, unitario):
        self.__unitario = unitario

    def set_total(self, total):
        self.__total = total


    def set_id_detallepedido(self):
        return self.__id_detallepedido 
    
    def set_id_pedido(self):
        return self.__id_pedido 

    def set_id_plato(self):
        return self.__id_plato 

    def set_unitario(self):
        return self.__unitario 

    def set_total(self):
        return self.__total