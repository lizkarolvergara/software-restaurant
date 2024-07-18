from model.plato import Plato
from model.detalle import Detalle

class DetalleOrden(Detalle):
    def __init__(self, id_detalleorden, id_orden, plato: Plato, cantidad, precio_unitario):
        super().__init__(cantidad, precio_unitario)
        self.id_detalleorden = id_detalleorden
        self.id_orden = id_orden
        self.plato = plato

    def descripcion(self):
        return f"Detalle Orden: {self.id_detalleorden}, Orden: {self.id_orden}, {self.plato.descripcion()}, {super().descripcion()}"
