""" Modules for Controlling Data Flow
    Use this controller only when using Mappy Type Format
"""

from Mappy.API import MysqlController, SQLBuilder
from flask import abort

class Controller():
    """ Class of controller
        All data flow is recommended using Mappy Format
    """

    def __init__(self, database_name, primary_key):
        self.internal_data = None
        self.database_name = database_name
        self.primary_key = primary_key

    def set(self, setter):
        self.internal_data = setter

    def get(self, data_id = False):
        """ Function for getting data from MySQL Database
            Output
                @route url/<endpoint> when you not provide id, it will fetch all the data
                @route url/<endpoint>/<id> when id provided, it will fetch specific data
        """
        sql_builder = SQLBuilder()

        if not data_id:
            sql_builder.select("*", self.database_name)
            self.internal_data = self.query(sql_builder.build()).data()
            return self

        sql_builder.select("*", self.database_name).where(f"`{self.primary_key}` = '{data_id}'")
        self.internal_data = self.query(sql_builder.build()).data()
        self.internal_data = self.internal_data[0] if len(self.internal_data) > 0 else {}
        return self

    def query_get(self, data_id = False):
        """ Function for getting data from MySQL Database
            Output
                @route url/<endpoint> when you not provide id, it will fetch all the data
                @route url/<endpoint>/<id> when id provided, it will fetch specific data
        """
        sql_builder = SQLBuilder()

        if not data_id:
            sql_builder.select("*", self.database_name)
            self.internal_data = self.query(sql_builder.build()).data()
            return self

        sql_builder.select("*", self.database_name).where(f"`{self.primary_key}` = '{data_id}'")
        self.internal_data = self.query(sql_builder.build()).data()
        self.internal_data = self.internal_data[0] if len(self.internal_data) > 0 else {}
        return self

    def empty(self):
        """ Function to empty the internal data
            Output
                Empty Data
        """
        self.internal_data = {}
        return self

    def data(self):
        """ Function for getting internal data directly without __dict__ """
        return self.internal_data

    def query(self, sql):
        """ Function for manipulating data with special case like create and Update
            Input
                SQL Commands
        """
        mysql_controller = MysqlController().set_sql(sql)
        self.internal_data = mysql_controller.execute()
        return self

    def is_data_exists(self):
        """ Validate if data is exists or not"""
        return bool(self.internal_data)

    @classmethod
    def trigger_error(cls, error_code):
        """ Function to trigger if an error happened """
        codes_dictionary = {
            "DATA_NOT_EXISTS" : {
                "msg" : "JSON data is not exists! Please make a get() request first",
                "code" : "DATA_NOT_EXISTS",
                "success" : False
            },
            "INVALID_DATA_TYPE" : {
                "msg" : "Form data should be object of JSON for mappy",
                "code" : "INVALID_DATA_TYPE",
                "success" : False
            }
        }
        abort(500, codes_dictionary[error_code])
