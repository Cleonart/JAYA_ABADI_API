from .interface.interface_barang import BarangInterface
from Router import Router

router = Router()
routes = [
	{
		"path" : "master/barang",
		"children" : BarangInterface().routes
	}
]

def register(api):
	router.register(api, routes)