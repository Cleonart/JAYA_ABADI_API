from Mappy.API.interface import MappyInterface
from ..controller.controller_order_pembelian import ControllerOrderPembelian

class InterfacePembelian(MappyInterface):
	def __init__(self):
		super().__init__(ControllerOrderPembelian)
		