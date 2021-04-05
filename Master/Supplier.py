from flask_restful import Resource,request
from mysql import connExecute
import random
from Universal.options import opt
from Universal.form import form
from Universal.table import tbl

class FormSupplier(Resource):

	def get(self, id):

		supplier_id       = "SUP" + str(random.randint(1000000,9999999))
		supplier_nama     = ""
		supplier_alamat   = ""
		supplier_provinsi = ""
		supplier_kota     = ""
		supplier_telepon  = ""

		if id != "baru":
			sql = "SELECT * FROM `master_supplier` WHERE `supplier_id` = '{}'".format(id)
			json_data = connExecute(sql)
			if len(json_data) > 0:
				json_data          = json_data[0]
				supplier_id        = json_data['supplier_id']
				supplier_nama      = json_data['supplier_nama'].title()
				supplier_alamat    = json_data['supplier_alamat']
				supplier_provinsi  = json_data['supplier_provinsi']
				supplier_kota      = json_data['supplier_kota']
				supplier_telepon   = json_data['supplier_telepon']

		supplier = form(supplier_id)
		supplier.add_text("Nama Supplier", "Masukan Nama Supplier", supplier_nama)
		supplier.add_text("Alamat Supplier", "Masukan Alamat Supplier", supplier_alamat)
		supplier.add_select("Provinsi Supplier", "Silahkan pilih provinsi", opt.provinsi(), supplier_provinsi)
		supplier.add_select("Kota Supplier", "Silahkan pilih kota", opt.kota(), supplier_kota)
		supplier.add_text("No. Telepon", "Masukan Nomor Telepon", supplier_telepon)
		return supplier.get()

	def post(self, id):
		data = request.get_json()

		supplier_id        = data[0]['value']
		supplier_nama      = data[1]['value']
		supplier_alamat    = data[2]['value']
		supplier_provinsi  = data[3]['value']
		supplier_kota      = data[4]['value']
		supplier_telepon   = data[5]['value']

		sql  = "INSERT INTO `master_supplier` SET "
		sql += "`supplier_id`       = '{}',".format(supplier_id)
		sql += "`supplier_nama`     = '{}',".format(supplier_nama.upper())
		sql += "`supplier_alamat`   = '{}',".format(supplier_alamat)
		sql += "`supplier_provinsi` = '{}',".format(supplier_provinsi)
		sql += "`supplier_kota`     = '{}',".format(supplier_kota)
		sql += "`supplier_telepon`  = '{}'".format(supplier_telepon)
		sql += "ON DUPLICATE KEY UPDATE "
		sql += "`supplier_nama`     = '{}',".format(supplier_nama.upper())
		sql += "`supplier_alamat`   = '{}',".format(supplier_alamat)
		sql += "`supplier_provinsi` = '{}',".format(supplier_provinsi)
		sql += "`supplier_kota`     = '{}',".format(supplier_kota)
		sql += "`supplier_telepon`  = '{}'".format(supplier_telepon)

		execs = connExecute(sql)
		return execs

class TabelSupplier(Resource):
	def get(self):
		sql  = "SELECT * FROM `master_supplier`"

		table_list = connExecute(sql);
		list_data  = []
		for data in table_list:
			table_data = tbl(data['supplier_id'])
			table_data.add_field_text(data['supplier_nama'].title())
			table_data.add_field_text(data['supplier_alamat'].title())
			table_data.add_field_text(data['supplier_provinsi'] + "/" + data['supplier_kota'])
			table_data.add_field_text(data['supplier_telepon'])
			list_data.append(table_data.get())	
		return list_data
