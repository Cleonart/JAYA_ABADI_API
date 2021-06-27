""" Interface
    Module for pre made controller to interface
"""

from flask_restful import Resource, request
from ..router import MappyRouter

class MappyInterface(MappyRouter):
    """ Handling Interfaces from Controller
        BarangInterface cosnsists of 3 main class, Form, Table and Data
        Form : Handling All Form for a data to be manipulated with Mapppy UI
        Table : Handling All Table for be viewed on Mappy Table UI
        Data : Handling All Data to be pulled from database
    """
    def __init__(self, api_controller):
        """ Initializitaion
            Initalize Controller
        """
        self.router = MappyRouter.__init__
        self.controller = api_controller()
        self.routes = [
            # @route /master/barang
            self.build_route("", self.Data, str(self.controller) + "data"),
            # @route /master/barang/<id>
            self.build_route("<string:data_id>", self.Data, str(self.controller) + "data_get_by_id"),
            # @route /master/barang/table
            self.build_route("table", self.Table, str(self.controller) + "tabel"),
            # @route /master/barang/form
            self.build_route("form", self.Form, str(self.controller) + "form_create"),
            # @route /master/barang/form/<id>
            self.build_route("form/<string:data_id>", self.Form, str(self.controller) + "form_get_by_id")
        ]

    def get_routes(self):
        """ Method for getting all the routes """
        return self.router

    def build_route(self, path, component, endpoint):
        """ Building the route with more simple way """
        return MappyRouter.route(path=path, \
                                component=component,\
                                endpoint=endpoint, \
                                payload={"controller" : self.controller})

    class Form(Resource):
        """ Handling Form Interfaces
            Input
                JSON via post request
            Output
                Mappy JSON format of Empty Form
                Mappy JSON format of Valued Form
        """
        def __init__(self, **kwargs):
            self.controller = kwargs["controller"]

        def get(self, data_id = False):
            """ Get Mappy Form Structure of Data, output will be in Mappy Form Format"""
            return self.controller.get(data_id).form()

        def post(self):
            """ Post Event for [CREATING, UPDATING] data """
            data = request.get_json()
            return self.controller.create(data)

    class Table(Resource):
        """ Handling Form Interfaces """
        def __init__(self, **kwargs):
            self.controller = kwargs["controller"]

        def get(self):
            """ Table Interface for getting full Mappy Format Table
                Output
                    Mappy JSON format of Table
            """
            return self.controller.table()

    class Data(Resource):
        """ Handling Data Interfaces
                Input
                    Get entire barang_data via @route http://url/master/barang
                    Get specific barang_data by specify id via @route http://url/master/barang/<id>
        """
        def __init__(self, **kwargs):
            self.controller = kwargs['controller']

        def get(self, data_id = False):
            """ Get Request for getting barang_data
                This get have various usages
                @route http://url/master/barang to get all data
                @route http://url/master/barang/<id> to get data with specific id
                @route http://url/master/barang/active to get data with active state
                @route http://url/master/barang/inactive to get data with inactive state
            """
            if data_id in ("active","inactive"):
                return self.controller.table_with_state(data_id)
            return self.controller.get(data_id).data()
