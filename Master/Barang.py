from flask_restful import Resource,request
from mysql import connExecute
import random
from Universal.options import opt
from Universal.form import form
from Universal.table import tbl

class FormBarang(Resource):

	def get(self, id):

		barang_id            = "B" + str(random.randint(1000000,9999999))
		barang_nama          = ""
		barang_kategori      = ""
		barang_merek         = ""
		barang_varian        = ""
		barang_satuan_eceran = ""
		barang_satuan_grosir = ""
		barang_harga_beli    = ""
		barang_harga_jual    = ""

		if id != "baru":
			sql = "SELECT * FROM `barang` WHERE `barang_id` = '{}'".format(id)
			json_data = connExecute(sql)
			if len(json_data) > 0:
				json_data            = json_data[0]
				barang_id            = json_data['barang_id']
				barang_nama          = json_data['barang_nama'].title()
				barang_merek         = json_data['barang_merek']
				barang_kategori      = json_data['barang_kategori']
				barang_varian        = json_data['barang_varian']
				barang_satuan_eceran = json_data['barang_satuan_eceran']
				barang_satuan_grosir = json_data['barang_satuan_grosir']
				barang_harga_beli    = json_data['barang_harga_beli']
				barang_harga_jual    = json_data['barang_harga_jual']

		barang = form(barang_id)
		barang.add_text("Nama Barang", "Masukan Nama Barang", barang_nama)
		barang.add_select("Kategori", "Masukan Kategori", opt.kategori(), barang_kategori)
		barang.add_select("Merek", "Masukan Nama Merek", opt.merek(), barang_merek)
		barang.add_text("Varian Barang", "Masukan Varian Barang", barang_varian)
		barang.add_select("Satuan Eceran", "Satuan Eceran Barang", opt.satuan(), barang_satuan_eceran)
		barang.add_select("Satuan Grosir", "Satuan Grosir Barang", opt.satuan(), barang_satuan_grosir)
		barang.add_text("Harga Beli", "Masukan Harga Beli", barang_harga_beli)
		barang.add_text("Harga Jual", "Masukan Harga Jual", barang_harga_jual)

		if id == "baru":
			barang.add_text("Stok Awal Toko", "Masukan Stok Awal", "")
			barang.add_text("Stok Awal Gudang", "Masukan Stok Awal Gudang", "")
		
		return barang.get()

	def post(self, id):
		data = request.get_json()

		barang_id            = data[0]['value']
		barang_nama          = data[1]['value']
		barang_kategori      = data[2]['value']
		barang_merek         = data[3]['value']
		barang_varian        = data[4]['value']
		barang_satuan_eceran = data[5]['value']
		barang_satuan_grosir = data[6]['value']
		barang_harga_beli    = data[7]['value']
		barang_harga_jual    = data[8]['value']

		sql  = "INSERT INTO `barang` SET "
		sql += "`barang_id`            = '{}',".format(barang_id)
		sql += "`barang_nama`          = '{}',".format(barang_nama.upper())
		sql += "`barang_kategori`      = '{}',".format(barang_kategori)
		sql += "`barang_varian`        = '{}',".format(barang_varian.upper())
		sql += "`barang_merek`         = '{}',".format(barang_merek)
		sql += "`barang_satuan_eceran` = '{}',".format(barang_satuan_eceran)
		sql += "`barang_satuan_grosir` = '{}',".format(barang_satuan_grosir)
		sql += "`barang_harga_beli`    = '{}',".format(barang_harga_beli)
		sql += "`barang_harga_jual`    = '{}'".format(barang_harga_jual)
		sql += "ON DUPLICATE KEY UPDATE "
		sql += "`barang_nama`          = '{}',".format(barang_nama.upper())
		sql += "`barang_kategori`      = '{}',".format(barang_kategori)
		sql += "`barang_varian`        = '{}',".format(barang_varian.upper())
		sql += "`barang_merek`         = '{}',".format(barang_merek)
		sql += "`barang_satuan_eceran` = '{}',".format(barang_satuan_eceran)
		sql += "`barang_satuan_grosir` = '{}',".format(barang_satuan_grosir)
		sql += "`barang_harga_beli`    = '{}',".format(barang_harga_beli)
		sql += "`barang_harga_jual`    = '{}'".format(barang_harga_jual)

		execs = connExecute(sql)
		return execs

class TabelBarang(Resource):
	def get(self):
		sql  = "SELECT * FROM `barang` as a "
		sql += "INNER JOIN `kategori` as b "
		sql += "ON a.barang_kategori = b.kategori_id "
		sql += "INNER JOIN `merek` as c "
		sql += "ON a.barang_merek = c.merek_id "

		table_list = connExecute(sql);
		list_data  = []
		for data in table_list:
			table_data = tbl(data['barang_id'])
			table_data.add_field_badge(data['kategori_nama'].title())
			table_data.add_field_text(data['barang_nama'].title())
			table_data.add_field_text(data['merek_nama'].title())
			table_data.add_field_text(data['barang_varian'])
			table_data.add_field_price(data['barang_harga_jual'])
			table_data.add_field_text(data['barang_stok_toko'])
			table_data.add_field_text(data['barang_stok_gudang'])
			list_data.append(table_data.get())	
		return list_data
