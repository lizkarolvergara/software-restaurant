from model.entidad import Entidad

class Proveedor(Entidad):
    def __init__(self, id_proveedor, denominacion, telefono, email):
        super().__init__(denominacion, telefono)
        self.id_proveedor = id_proveedor
        self.email = email
    
    def datos(self):
        return f"RUC: {self.id_proveedor}, Proveedor {super().datos()}, Email: {self.email}"


