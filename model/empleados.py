class Empleado:
    def __init__(self, id_empleado, denominacion, cargo, usuario, contrasena, telefono):
        self.id_empleado = id_empleado
        self.denominacion = denominacion
        self.cargo = cargo
        self.usuario = usuario
        self.contrasena = contrasena
        self.telefono = telefono
    
    def set_id_empleado(self, id_empleado):
        self.__id_empleado = id_empleado
    
    def set_denominacion(self, denominacion):
        self.__denominacion = denominacion

    def set_cargo(self, cargo):
        self.__cargo = cargo

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def set_contrasena(self, contrasena):
        self.__contrasena = contrasena

    def set__telefono(self, telefono):
        self.set__telefono = telefono
    



    def set_id_empleado(self):
        return self.__id_empleado
    
    def set_denominacion(self):
        return self.__denominacion

    def set_cargo(self):
        return self.__cargo
    
    def set_usuario(self):
        return self.__usuario 

    def set_contrasena(self):
        return self.__contrasena 
    
    def set_telefono(self):
        return self.__telefono
    
    