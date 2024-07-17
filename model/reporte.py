class Reporte:
    def __init__(self, id_reporte, fechageneracion, contenido):
        self.id_reporte = id_reporte
        self.fechageneracion = fechageneracion
        self.contenido = contenido

    def set_id_reporte(self, id_reporte):
        self.__id_reporte = id_reporte
    
    def set_fechageneracion(self, fechageneracion):
        self.__fechageneracion = fechageneracion

    def set_contenido(self, contenido):
        self.__contenido = contenido
    


    def set_id_reporte(self):
        return self.__id_reporte
    
    def set_fechageneracion(self,):
        return self.__fechageneracion

    def set_contenido(self):
        return self.__contenido

