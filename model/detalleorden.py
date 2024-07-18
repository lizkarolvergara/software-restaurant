class DetalleOrden:
    def __init__(self, id_detalleorden, id_orden, id_plato, cantidad, unitario, total):
        self.id_detalleorden = id_detalleorden
        self.id_orden = id_orden
        self.id_plato = id_plato
        self.cantidad = cantidad
        self.unitario = unitario
        self.total = total

    def set_id_orden(self, id_orden):
        self.__id_orden = id_orden
    
    def set_id_orden(self, id_orden):
        self.__id_orden = id_orden

    def set_id_plato(self, id_plato):
        self.__id_plato = id_plato

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_unitario(self, unitario):
        self.__unitario = unitario

    def set_total(self, total):
        self.__total = total




    def set_id_orden(self):
        return self.__id_orden
    
    def set_id_orden(self):
        return self.__id_orden 

    def set_id_plato(self):
        return self.__id_plato 

    def set_cantidad(self):
        return self.__cantidad 

    def set_unitario(self):
        return self.__unitario
    
    def set_total(self):
        return self.__total