from flask_restful import Resource,request
from mysql import connExecute
import random
from Universal.options import opt
from Universal.form import form
from Universal.table import tbl

class FormMerek(Resource):

	def get(self, id):

		merek_id   = "M" + str(random.randint(10000,99999))
		merek_nama = ""

		if id != "baru":
			sql = "SELECT * FROM `merek` WHERE `merek_id` = '{}'".format(id)
			json_data = connExecute(sql)
			if len(json_data) > 0:
				json_data    = json_data[0]
				merek_id    = json_data['merek_id']
				merek_nama  = json_data['merek_nama'].title()

		merek = form(merek_id)
		merek.add_text("Nama Merek", "Masukan Nama Merek", merek_nama)
		return merek.get()

	def post(self, id):

		data = request.get_json()
		merek_id    = data[0]['value']
		merek_nama  = data[1]['value']

		sql  = "INSERT INTO `merek` SET "
		sql += "`merek_id`            = '{}',".format(merek_id)
		sql += "`merek_nama`          = '{}'".format(merek_nama.upper())
		sql += "ON DUPLICATE KEY UPDATE "
		sql += "`merek_nama`          = '{}'".format(merek_nama.upper())

		execs = connExecute(sql)
		return execs

class TabelMerek(Resource):
	def get(self):
		sql  = "SELECT * FROM `merek`"

		table_list = connExecute(sql);
		list_data  = []
		for data in table_list:
			table_data = tbl(data['merek_id'])
			table_data.add_field_text(data['merek_nama'].title())
			list_data.append(table_data.get())	
		return list_data