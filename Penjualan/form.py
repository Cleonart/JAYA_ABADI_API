from functions import Options, Form, generateId
from flask_restful import Resource,request
from mysql import connExecute

class FormPenjualan(Resource):
	""" Form for handling 'penjualan '"""

	def get(self, id):
		""" 
			Handling GET request from gateway: 
			/penjualan/order/baru
			/penjualan/order/{ID}
		"""
		
		# Get raw data from server
		json_data = {}
		json_data['data_supplier'] = Options.objectDataSupplier()
		json_data['data_product']  = Options.objectDataBarang()
		json_data['data_satuan']   = Options.objectDataSatuan()

		if id == "":

		return json_data

	def post(self):
		"""
			Handling POST request from gateway:
			/penjualan/order/baru
			/penjualan/order/{ID} 
		"""
		