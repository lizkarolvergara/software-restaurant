class Detalle:
    def __init__(self, cantidad, precio_unitario, total):
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.total = total

    def descripcion(self):
        return f"{self.cantidad}, {self.precio_unitario}, {self.total}"
    