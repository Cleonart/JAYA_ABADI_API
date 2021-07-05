""" Master Package
    This package consists of router and 3 interface :
    @route order/pembelian
    @route order/penjualan
    @route order/pos
"""

from Mappy.router import MappyRouter
from Mappy.API.interface import MappyInterface
from .interface.interface_pembelian import InterfacePembelian
from .interface.interface_penjualan import InterfacePenjualan
from .interface.interface_pos import InterfacePos

interface_pembelian = InterfacePembelian()
interface_penjualan = InterfacePenjualan()
interface_pos = InterfacePos()

router = MappyRouter()
routes = [
    {
        "path" : "order/pembelian",
        "children" : interface_pembelian.routes
    },
    {
        "path" : "order/penjualan",
        "children" : interface_penjualan.routes
    },
    {
        "path" : "order/pos",
        "children" : interface_pos.routes
    }
]


def register(api):
    """ Embedded Function to register all routes """
    router.register(api, routes)