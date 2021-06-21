from .interface.BarangInterface import BarangDataInterface
from Router import Router

router = Router()
routes = [
	{
		"path" : "master/barang",
		"children" : [
			{
				"path" : 
			}
		]
	}
]

def register(api):
	router.register(api, routes)