from flask_restful import Resource,request
from mysql import connExecute
import random
from Universal.options import opt
from Universal.form import form
from Universal.table import tbl

class FormKategori(Resource):

	def get(self, id):
		kategori_id   = "K" + str(random.randint(100000,999999))
		kategori_nama = ""

		if id != "baru":
			sql = "SELECT * FROM `kategori` WHERE `kategori_id` = '{}'".format(id)
			json_data = connExecute(sql)
			if len(json_data) > 0:
				json_data     = json_data[0]
				kategori_id   = json_data['kategori_id']
				kategori_nama = json_data['kategori_nama'].title()
		
		kategori = form(kategori_id)
		kategori.add_text("Nama Kategori", "Masukan Nama Kategori", kategori_nama)
		return kategori.get()

	def post(self, id):

		data = request.get_json()
		kategori_id    = data[0]['value']
		kategori_nama  = data[1]['value']

		sql  = "INSERT INTO `kategori` SET "
		sql += "`kategori_id`    = '{}',".format(kategori_id)
		sql += "`kategori_nama`  = '{}'".format(kategori_nama.upper())
		sql += "ON DUPLICATE KEY UPDATE "
		sql += "`kategori_nama`  = '{}'".format(kategori_nama.upper())

		execs = connExecute(sql)
		return execs

class TabelKategori(Resource):
	def get(self):
		sql  = "SELECT * FROM `kategori`"

		table_list = connExecute(sql);
		list_data  = []
		for data in table_list:
			table_data = tbl(data['kategori_id'])
			table_data.add_field_text(data['kategori_nama'].title())
			list_data.append(table_data.get())	
		return list_data