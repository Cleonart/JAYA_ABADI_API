from flask_restful import Resource,request
from mysql import connExecute
import random
from Universal.options import opt
from Universal.form import form
from Universal.table import tbl

class FormPelanggan(Resource):

	def get(self, id):

		pelanggan_id     = "PEL" + str(random.randint(1000000,9999999))
		pelanggan_nama   = ""
		pelanggan_alamat = ""
		pelanggan_kontak = ""

		if id != "baru":
			sql = "SELECT * FROM `master_pelanggan` WHERE `pelanggan_id` = '{}'".format(id)
			json_data = connExecute(sql)
			if len(json_data) > 0:
				json_data         = json_data[0]
				pelanggan_id      = json_data['pelanggan_id']
				pelanggan_nama    = json_data['pelanggan_nama'].title()
				pelanggan_alamat  = json_data['pelanggan_alamat']
				pelanggan_kontak  = json_data['pelanggan_kontak']

		pelanggan = form(pelanggan_id)
		pelanggan.add_text("Nama Pelanggan", "Masukan Nama Pelanggan", pelanggan_nama)
		pelanggan.add_text("Alamat Pelanggan", "Masukan Alamat Pelanggan", pelanggan_alamat)
		pelanggan.add_text("Kontak Pelanggan", "Masukan Kontak Pelanggan", pelanggan_kontak)
		return pelanggan.get()

	def post(self, id):
		data = request.get_json()

		pelanggan_id     = data[0]['value']
		pelanggan_nama   = data[1]['value']
		pelanggan_alamat = data[2]['value']
		pelanggan_kontak = data[3]['value']

		sql  = "INSERT INTO `master_pelanggan` SET "
		sql += "`pelanggan_id`      = '{}',".format(pelanggan_id)
		sql += "`pelanggan_nama`    = '{}',".format(pelanggan_nama.upper())
		sql += "`pelanggan_alamat`  = '{}',".format(pelanggan_alamat)
		sql += "`pelanggan_kontak`  = '{}'".format(pelanggan_kontak)
		sql += "ON DUPLICATE KEY UPDATE "
		sql += "`pelanggan_nama`    = '{}',".format(pelanggan_nama.upper())
		sql += "`pelanggan_alamat`  = '{}',".format(pelanggan_alamat)
		sql += "`pelanggan_kontak`  = '{}'".format(pelanggan_kontak)

		execs = connExecute(sql)
		return execs

class TabelPelanggan(Resource):
	def get(self):
		sql  = "SELECT * FROM `master_pelanggan`"

		table_list = connExecute(sql);
		list_data  = []
		for data in table_list:
			table_data = tbl(data['pelanggan_id'])
			table_data.add_field_text(data['pelanggan_nama'].title())
			table_data.add_field_text(data['pelanggan_alamat'].title())
			table_data.add_field_text(data['pelanggan_kontak'])
			list_data.append(table_data.get())	
		return list_data
