from Mappy.API.interface import MappyInterface
from ..controller.controller_order_penjualan import ControllerOrderPenjualan

class InterfacePenjualan(MappyInterface):
	def __init__(self):
		super().__init__(ControllerOrderPenjualan)
		