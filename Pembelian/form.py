from flask_restful import Resource,request
from mysql import connExecute
import random
from Universal.options import opt
from Universal.form import form
from Universal.table import tbl

class FormPembelian(Resource):

	def get(self, id):
		json_data = {}
		json_data['data_supplier'] = connExecute("SELECT * FROM `master_supplier`")
		return json_data