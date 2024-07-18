class Plato:
    def __init__(self, id_plato, nombre, descripcion, precio, disponibilidad):
        self.id_plato = id_plato
        self.nombre = nombre
        self.descripcion_plato = descripcion
        self.precio = precio
        self.disponibilidad = disponibilidad

    def descripcion(self):
        return f"Plato: {self.nombre}, Descripción: {self.descripcion_plato}, Precio: {self.precio}, Disponibilidad: {self.disponibilidad}"
