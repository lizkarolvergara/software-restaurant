from model.entidad import Entidad

class Empleado(Entidad):
    def __init__(self, id_empleado, denominacion, cargo, usuario, contrasena, telefono):
        super().__init__(denominacion, telefono)
        self.id_empleado = id_empleado
        self.cargo = cargo
        self.usuario = usuario
        self.contrasena = contrasena

    def datos(self):
        return f"Nombre: {self.id_empleado}, Cargo: {self.cargo}, {super().datos()}, Usuario: {self.usuario}, Contraseña: {self.contrasena}"
    
    