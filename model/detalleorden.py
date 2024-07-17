class Orden:
    def __init__(self, id_orden, id_empleado, id_mesa, fecha_hora, estado):
        self.id_orden = id_orden
        self.id_empleado = id_empleado
        self.id_mesa = id_mesa
        self.fecha_hora = fecha_hora
        self.estado = estado

    def set_id_orden(self, id_orden):
        self.__id_orden = id_orden
    
    def set_id_empleado(self, id_empleado):
        self.__id_empleado = id_empleado

    def set_id_mesa(self, id_mesa):
        self.__id_mesa = id_mesa

    def set_fecha_hora(self, fecha_hora):
        self.__fecha_hora = fecha_hora

    def set_estado(self, estado):
        self.__estado = estado


    def set_id_orden(self):
        return self.__id_orden
    
    def set_id_empleado(self):
        return self.__id_empleado 

    def set_id_mesa(self):
        return self.__id_mesa 

    def set_fecha_hora(self):
        return self.__fecha_hora 

    def set_estado(self):
        return self.__estado