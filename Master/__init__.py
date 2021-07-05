""" Master Package
    This package consists of router and 4 interface :
    @route master/barang
    @route master/pelanggan
    @route master/supplier
    @route master/pengguna
"""

from Mappy.API.interface import MappyInterface
from Mappy.router import MappyRouter
from .components.controller_barang import ControllerBarang
from .components.controller_pelanggan import ControllerPelanggan
from .components.controller_pengguna import ControllerPengguna
from .components.controller_supplier import ControllerSupplier

# Make instance of interfaces
interface_barang = MappyInterface(ControllerBarang)
interface_pelanggan = MappyInterface(ControllerPelanggan)
interface_pengguna = MappyInterface(ControllerPengguna)
interface_supplier = MappyInterface(ControllerSupplier)

router = MappyRouter()
routes = [
    {
        "path" : "master/barang",
        "children" : interface_barang.routes
    },
    {
        "path" : "master/pelanggan",
        "children" : interface_pelanggan.routes
    },
    {
        "path" : "master/pengguna",
        "children" : interface_pengguna.routes
    },
    {
        "path" : "master/supplier",
        "children" : interface_supplier.routes
    }
]

def register(api):
    """ Embedded Function to register all routes """
    router.register(api, routes)
