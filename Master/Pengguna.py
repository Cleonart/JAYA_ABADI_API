from flask_restful import Resource,request
from mysql import connExecute
import random
from Universal.options import opt
from Universal.form import form
from Universal.table import tbl

class FormPengguna(Resource):

	def get(self, id):

		pengguna_id     = "USR" + str(random.randint(10000,99999))
		pengguna_nama   = ""
		pengguna_posisi = ""
		pengguna_status = ""
		
		if id != "baru":
			sql = "SELECT * FROM `pengguna` WHERE `pengguna_id` = '{}'".format(id)
			json_data = connExecute(sql)
			if len(json_data) > 0:
				json_data        = json_data[0]
				pengguna_id      = json_data['pengguna_id']
				pengguna_nama    = json_data['pengguna_nama'].upper()
				pengguna_posisi  = json_data['pengguna_posisi']
				pengguna_status  = json_data['pengguna_status']

		pengguna = form(pengguna_id)
		pengguna.add_text("Nama Pengguna", "Masukan Nama Pengguna", pengguna_nama)
		pengguna.add_select("Pilih Posisi Pengguna", "Posisi Pengguna", opt.posisi(), pengguna_posisi)
		pengguna.add_select("Pilih Status Pengguna", "Pilih Status Pengguna", opt.status(), pengguna_status)
		return pengguna.get()

	def post(self, id):

		data = request.get_json()
		pengguna_id      = data[0]['value']
		pengguna_nama    = data[1]['value']
		pengguna_posisi  = data[2]['value']
		pengguna_status  = data[3]['value']

		sql  = "INSERT INTO `pengguna` SET "
		sql += "`pengguna_id`      = '{}',".format(pengguna_id)
		sql += "`pengguna_nama`    = '{}',".format(pengguna_nama.upper())
		sql += "`pengguna_posisi`  = '{}',".format(pengguna_posisi)
		sql += "`pengguna_status`  = '{}' ".format(pengguna_status)
		sql += "ON DUPLICATE KEY UPDATE "
		sql += "`pengguna_nama`    = '{}',".format(pengguna_nama.upper())
		sql += "`pengguna_posisi`  = '{}',".format(pengguna_posisi)
		sql += "`pengguna_status`  = '{}' ".format(pengguna_status)

		execs = connExecute(sql)
		return execs

class TabelPengguna(Resource):
	def get(self, list_data = []):
		list_data = [];
		for data in connExecute("SELECT * FROM `pengguna` as a INNER JOIN `posisi` as b ON a.pengguna_posisi = b.posisi_id"):
			table_data = tbl(data['pengguna_id'])
			table_data.add_field_text(data['pengguna_nama'].title())
			table_data.add_field_text(data['posisi_nama'])
			table_data.add_field_text(data['pengguna_status'])
			list_data.append(table_data.get())	
		return list_data