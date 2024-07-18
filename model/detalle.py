class Detalle:
    def __init__(self, cantidad, precio_unitario):
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.total = cantidad * precio_unitario

    def descripcion(self):
        return f"Cantidad: {self.cantidad}, P.U.: {self.precio_unitario}, Total: {self.total}"
