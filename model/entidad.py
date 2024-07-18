class Entidad:
    def __init__(self, denominacion, telefono):
        self.denominacion = denominacion
        self.telefono = telefono

    def datos(self):
        return f"Denominación: {self.denominacion}, Teléfono: {self.telefono}"
