from model.cliente import Cliente
from model.proveedor import Proveedor
from model.detalleorden import DetalleOrden
from model.detallepedido import DetallePedido
from model.plato import Plato

objCliente = Cliente(70233218, "Liz Vergara", 975203430)
print(objCliente.datos())  

objProveedor = Proveedor(20606185775, "AMAZE PERU E.I.R.L.", "contacto@amazeperu.com", 961561310)
print(objProveedor.datos())  

# objeto Plato
plato = Plato("PL001", "Sopa Wantan", "Sopa con wantan y fideos", 15, True)

objDetalleOrden = DetalleOrden("OR001", 1001, plato, 2, 15)
print(objDetalleOrden.descripcion())  

objDetallePedido = DetallePedido("PE001", 2001, plato, 3, 15)
print(objDetallePedido.descripcion()) 
