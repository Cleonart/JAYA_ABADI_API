""" Master Package
    This package consists of router and 4 interface :
    @route master/barang
    @route master/pelanggan
    @route master/supplier
    @route master/pengguna
"""

from Router import Router
from .interface.interface_barang import InterfaceBarang

# Make instance of interfaces
interface_barang = InterfaceBarang()

router = Router()
routes = [
    {
        "path" : "master/barang",
        "children" : interface_barang.routes
    }
]

def register(api):
    """ Embedded Function to register all routes """
    router.register(api, routes)
