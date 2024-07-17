class Empleado:
    def __init__(self, id_empleado, nombre, apellido, cargo, usuario, contrasena):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo
        self.usuario = usuario
        self.contrasena = contrasena
    
    def set_id_empleado(self, id_empleado):
        self.__id_empleado = id_empleado
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def set_contrasena(self, contrasena):
        self.__contrasena = contrasena

    
    def set_id_empleado(self):
        return self.__id_empleado
    
    def set_nombre(self):
        return self.__nombre

    def set_apellido(self):
        return self.__apellido 

    def set_usuario(self):
        return self.__usuario 

    def set_contrasena(self):
        return self.__contrasena 