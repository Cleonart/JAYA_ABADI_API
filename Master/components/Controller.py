from mysql import MysqlController
from flask import abort

class Controller():

	ERROR = {}
	
	def __init__(self, db_name, primary_key):
		self.db_name = db_name
		self.primary_key = primary_key

	def get(self, id=False):
		""" Function for getting data from MySQL Database """

		# Make Mysql Controller instance
		mysql_controller = MysqlController()

		# Fetching all data without specify ID
		if not id:
			mysql_controller.set_sql("SELECT * FROM `{}`".format(self.db_name))
			self.internal_data = mysql_controller.execute()
			return self

		# Fetching all data with specific ID
		mysql_controller.set_sql("SELECT * FROM `{}` WHERE `{}` = '{}'".format(self.db_name, self.primary_key, id))
		self.internal_data = mysql_controller.execute()
		self.internal_data = self.internal_data[0] if len(self.internal_data) > 0 else {}
		return self

	def query(self, sql):

		# Make Mysql Controller instance
		mysql_controller = MysqlController()

		# Process data with specific query
		mysql_controller.set_sql(self.sql_all)
		self.internal_data = mysql_controller.execute()

	def raw(self):
		""" Function to convert get() object data to raw JSON data """
		if self.is_data_valid():
			return self.internal_data

	def is_data_valid(self):
		""" Make sure the internal data not corrupted """
		if not self.internal_data:
			self.ERROR['msg'] = "JSON Data is not exists! Please make a get() request first"
			self.ERROR['code'] = "DATA_NOT_EXISTS"
			self.ERROR['success'] = False
			abort(500, self.ERROR)
			return False
		return True

	def is_data_exists(self):
		return bool(self.internal_data)