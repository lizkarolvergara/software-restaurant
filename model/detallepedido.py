from model.plato import Plato
from model.detalle import Detalle

class DetallePedido(Detalle):
    def __init__(self, id_detallepedido, id_pedido, plato: Plato, cantidad, precio_unitario):
        super().__init__(cantidad, precio_unitario)
        self.id_detallepedido = id_detallepedido
        self.id_pedido = id_pedido
        self.plato = plato

    def descripcion(self):
        return f"Detalle Pedido: {self.id_detallepedido}, Pedido: {self.id_pedido}, {self.plato.descripcion()}, {super().descripcion()}"
