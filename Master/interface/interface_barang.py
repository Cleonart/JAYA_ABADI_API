""" Module Documentation
    Module already tested with pylint [6.30/10]
"""

from flask_restful import Resource, request
from Router import Router
from ..components.ControllerBarang import ControllerBarang

controller = ControllerBarang()

class BarangInterface(Router):
    """ Handling Interfaces from Controller
        BarangInterface cosnsists of 3 main class, Form, Table and Data
        Form : Handling All Form for a data to be manipulated with Mapppy UI
        Table : Handling All Table for be viewed on Mappy Table UI
        Data : Handling All Data to be pulled from database
    """
    def __init__(self):
        self.router = super().__init__
        self.routes = [
            # @route /master/barang
            self.build_route("", self.Data, "data"),
            # @route /master/barang/<id>
            self.build_route("<string:barang_id>", self.Data, "data_get_by_id"),
            # @route /master/barang/table
            self.build_route("table", self.Table, "tabel"),
            # @route /master/barang/form
            self.build_route("form", self.Form, "form_create"),
            # @route /master/barang/form/<id>
            self.build_route("form/<string:barang_id>", self.Form, "form_get_by_id")
        ]

    def get_routes(self):
        """ Method for getting all the routes """
        return self.routes

    def build_route(self, path, component, endpoint):
        """ Building the route with more simple way """
        return super().route(path=path, component=component, endpoint=endpoint)

    class Form(Resource):
        """ Handling Form Interfaces
            Input
                JSON via post request
            Output
                Mappy JSON format of Empty Form
                Mappy JSON format of Valued Form
        """
        @classmethod
        def get(cls, barang_id = False):
            """ Get Mappy Form Structure of Data, output will be in Mappy Form Format"""
            return controller.get(barang_id).form()

        @classmethod
        def post(cls):
            """ Post Event for [CREATING, UPDATING] data """
            data = request.get_json()
            print(data)
            return controller.create()

    class Table(Resource):
        """ Handling Form Interfaces """
        @classmethod
        def get(cls):
            """ Table Interface for getting full Mappy Format Table
                Output
                    Mappy JSON format of Table
            """
            return controller.table()

    class Data(Resource):
        """ Handling Data Interfaces
                Input
                    Get entire barang_data via @route http://url/master/barang
                    Get specific barang_data by specify id via @route http://url/master/barang/<id>
        """
        @classmethod
        def get(cls, barang_id = False):
            """ Get Request for getting barang_data
                This get have various usages
                @route http://url/master/barang to get all data
                @route http://url/master/barang/<id> to get data with specific id
                @route http://url/master/barang/active to get data with active state
                @route http://url/master/barang/inactive to get data with inactive state
            """
            if barang_id in ("active","inactive"):
                return controller.table_with_state(barang_id)
            return controller.get(barang_id).data()
#class FormBarang(Resource):

#   def post(self, id):

#       data = request.get_json()
#       barang_id = data[0]['value']
#       barang_nama = data[1]['value']
#       barang_kategori = data[2]['value']
#       barang_merek = data[3]['value']
#       barang_varian = data[4]['value']
#       barang_satuan_eceran = data[5]['value']
#       barang_satuan_grosir = data[6]['value']
#       barang_harga_beli = data[7]['value']
#       barang_harga_jual = data[8]['value']
#       """
#       if len(data) > 9:
#           barang_stok_toko     = data[9]['value']
#           barang_stok_gudang   = data[10]['value']
#
#       sql  = "INSERT INTO `barang` SET "
#       sql += "`barang_id`            = '{}',".format(barang_id)
#       sql += "`barang_nama`          = '{}',".format(barang_nama.upper())
#       sql += "`barang_kategori`      = '{}',".format(barang_kategori)
#       sql += "`barang_varian`        = '{}',".format(barang_varian.upper())
#       sql += "`barang_merek`         = '{}',".format(barang_merek)
#       sql += "`barang_satuan_eceran` = '{}',".format(barang_satuan_eceran)
#       sql += "`barang_satuan_grosir` = '{}',".format(barang_satuan_grosir)
#       sql += "`barang_harga_beli`    = '{}',".format(barang_harga_beli)
#       sql += "`barang_harga_jual`    = '{}'".format(barang_harga_jual)
#       if len(data) > 9:
#           sql += ",`barang_stok_toko`    = '{}',".format(barang_stok_toko)
#           sql += "`barang_stok_gudang`   = '{}'".format(barang_stok_gudang)
#
#       sql += "ON DUPLICATE KEY UPDATE "
#       sql += "`barang_nama`          = '{}',".format(barang_nama.upper())
#       sql += "`barang_kategori`      = '{}',".format(barang_kategori)
#       sql += "`barang_varian`        = '{}',".format(barang_varian.upper())
#       sql += "`barang_merek`         = '{}',".format(barang_merek)
#       sql += "`barang_satuan_eceran` = '{}',".format(barang_satuan_eceran)
#       sql += "`barang_satuan_grosir` = '{}',".format(barang_satuan_grosir)
#       sql += "`barang_harga_beli`    = '{}',".format(barang_harga_beli)
#       sql += "`barang_harga_jual`    = '{}'".format(barang_harga_jual)
#       if len(data) > 9:
#           sql += ",`barang_stok_toko`    = '{}',".format(barang_stok_toko
#           sql += "`barang_stok_gudang`   = '{}'".format(barang_stok_gudang))
#           """
#       #return connExecute(sql)
