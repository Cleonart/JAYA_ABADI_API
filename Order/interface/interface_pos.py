from Mappy.API.interface import MappyInterface
from ..controller.controller_order_pos import ControllerOrderPos

class InterfacePos(MappyInterface):
	def __init__(self):
		super().__init__(ControllerOrderPos)