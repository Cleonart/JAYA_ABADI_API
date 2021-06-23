from mysql import MysqlController
from flask import abort

class Controller():

	ERROR = {}
	
	def __init__(self, db_name, primary_key):
		self.db_name = db_name
		self.primary_key = primary_key

	def get(self, id = False):
		""" Function for getting data from MySQL Database """
		mysql_controller = MysqlController()
		print("get")
		if not id:
			mysql_controller.set_sql("SELECT * FROM `{}`".format(self.db_name))
			self.internal_data = mysql_controller.execute()
			return self
		
		mysql_controller.set_sql("SELECT * FROM `{}` WHERE `{}` = '{}'".format(self.db_name, self.primary_key, id))
		self.internal_data = mysql_controller.execute()
		print(self.internal_data)
		self.internal_data = self.internal_data[0] if len(self.internal_data) > 0 else {}
		return self

	def empty(self):
		self.internal_data = {}
		return self

	def data(self):
		""" Function for getting internal data directly without __dict__ """
		return self.internal_data

	def query(self, sql):

		# Make Mysql Controller instance
		mysql_controller = MysqlController()

		# Process data with specific query
		mysql_controller.set_sql(sql)
		self.internal_data = mysql_controller.execute()
		return self

	def raw(self):
		""" Function to convert get() object data to raw JSON data """
		if self.is_data_exists():
			return self.internal_data

	def is_data_exists(self):
		return bool(self.internal_data)

	def trigger_error(self, error_code):

		ERROR = {

			# Trigerred when data not exists
			"DATA_NOT_EXISTS" : {
				"msg" : "JSON data is not exists! Please make a get() request first",
				"code" : "DATA_NOT_EXISTS",
				"success" : False
			},

			# Triggered if form data format is not valid mappy form format
			"INVALID_DATA_TYPE" : {
				"msg" : "Form data should be object of JSON for mappy",
				"code" : "INVALID_DATA_TYPE",
				"success" : False
			}
		}

		abort(500, ERROR[error_code])

