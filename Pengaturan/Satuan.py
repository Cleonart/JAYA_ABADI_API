from flask_restful import Resource,request
from mysql import connExecute
import random
from Universal.options import opt
from Universal.form import form
from Universal.table import tbl

class FormSatuan(Resource):

	def get(self, id):

		satuan_id   = "S" + str(random.randint(10000,99999))
		satuan_nama = ""

		if id != "baru":
			sql = "SELECT * FROM `satuan` WHERE `satuan_id` = '{}'".format(id)
			json_data = connExecute(sql)
			if len(json_data) > 0:
				json_data    = json_data[0]
				satuan_id    = json_data['satuan_id']
				satuan_nama  = json_data['satuan_nama'].title()

		satuan = form(satuan_id)
		satuan.add_text("Nama Satuan", "Masukan Nama Satuan", satuan_nama)
		return satuan.get()

	def post(self, id):

		data = request.get_json()
		satuan_id    = data[0]['value']
		satuan_nama  = data[1]['value']

		sql  = "INSERT INTO `satuan` SET "
		sql += "`satuan_id`            = '{}',".format(satuan_id)
		sql += "`satuan_nama`          = '{}'".format(satuan_nama.upper())
		sql += "ON DUPLICATE KEY UPDATE "
		sql += "`satuan_nama`          = '{}'".format(satuan_nama.upper())

		execs = connExecute(sql)
		return execs

class TabelSatuan(Resource):
	def get(self):
		sql  = "SELECT * FROM `satuan`"

		table_list = connExecute(sql);
		list_data  = []
		for data in table_list:
			table_data = tbl(data['satuan_id'])
			table_data.add_field_text(data['satuan_nama'].title())
			list_data.append(table_data.get())	
		return list_data