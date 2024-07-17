class PedidoProveedor:
    def __init__(self, id_pedido, id_proveedor, fechapedido, fecharecepcion, estado):
        self.id_pedido = id_pedido
        self.id_proveedor = id_proveedor
        self.fechapedido = fechapedido
        self.fecharecepcion = fecharecepcion
        self.estado = estado

    def set_id_pedido(self, id_pedido):
        self.__id_pedido = id_pedido
    
    def set_id_proveedor(self, id_proveedor):
        self.__id_proveedor = id_proveedor

    def set_fechapedido(self, fechapedido):
        self.__fechapedido = fechapedido

    def set_fecharecepcion(self, fecharecepcion):
        self.__fecharecepcion = fecharecepcion

    def set_estado(self, estado):
        self.__estado = estado



    def set_id_pedido(self):
        return self.__id_pedido
    
    def set_id_proveedor(self):
        return self.__id_proveedor

    def set_fechapedido(self):
        return self.__fechapedido

    def set_fecharecepcion(self):
        return self.__fecharecepcion

    def set_estado(self, estado):
        return self.__estado 