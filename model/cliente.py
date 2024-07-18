from model.entidad import Entidad

class Cliente(Entidad):
    def __init__(self, id_cliente, denominacion, telefono):
        super().__init__(denominacion, telefono)
        self.id_cliente = id_cliente

    def datos(self):
        return f"DNI/RUC: {self.id_cliente}, Cliente {super().datos()}"
