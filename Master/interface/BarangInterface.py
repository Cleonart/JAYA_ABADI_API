from functions import Form, Options, Table, generateId
from flask_restful import Resource,request
from mysql import connExecute
from ..components.BarangController import BarangController

class FormBarang(Resource):

	def get(self, id):

		barang_id            = generateId("B")
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

		barang = Form(barang_id)
		barang.add_text("Nama Barang", "Masukan Nama Barang", barang_nama)
		barang.add_select("Kategori", "Masukan Kategori", Options.kategori(), barang_kategori)
		barang.add_select("Merek", "Masukan Nama Merek", Options.merek(), barang_merek)
		barang.add_text("Varian Barang", "Masukan Varian Barang", barang_varian)
		barang.add_select("Satuan Eceran", "Satuan Eceran Barang", Options.satuan(), barang_satuan_eceran)
		barang.add_select("Satuan Grosir", "Satuan Grosir Barang", Options.satuan(), barang_satuan_grosir)
		barang.add_text("Harga Beli", "Masukan Harga Beli", barang_harga_beli)
		barang.add_text("Harga Jual", "Masukan Harga Jual", barang_harga_jual)

		if id == "baru":
			barang.add_text("Stok Awal Toko", "Masukan Stok Awal", 0)
			barang.add_text("Stok Awal Gudang", "Masukan Stok Awal Gudang", 0)
		
		return barang.get()

	def post(self, id):

		data = request.get_json()
		barang_id = data[0]['value']
		barang_nama = data[1]['value']
		barang_kategori = data[2]['value']
		barang_merek = data[3]['value']
		barang_varian = data[4]['value']
		barang_satuan_eceran = data[5]['value']
		barang_satuan_grosir = data[6]['value']
		barang_harga_beli = data[7]['value']
		barang_harga_jual = data[8]['value']

		if len(data) > 9:
			barang_stok_toko     = data[9]['value']
			barang_stok_gudang   = data[10]['value']

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
		if len(data) > 9:
			sql += ",`barang_stok_toko`    = '{}',".format(barang_stok_toko)
			sql += "`barang_stok_gudang`   = '{}'".format(barang_stok_gudang)

		sql += "ON DUPLICATE KEY UPDATE "
		sql += "`barang_nama`          = '{}',".format(barang_nama.upper())
		sql += "`barang_kategori`      = '{}',".format(barang_kategori)
		sql += "`barang_varian`        = '{}',".format(barang_varian.upper())
		sql += "`barang_merek`         = '{}',".format(barang_merek)
		sql += "`barang_satuan_eceran` = '{}',".format(barang_satuan_eceran)
		sql += "`barang_satuan_grosir` = '{}',".format(barang_satuan_grosir)
		sql += "`barang_harga_beli`    = '{}',".format(barang_harga_beli)
		sql += "`barang_harga_jual`    = '{}'".format(barang_harga_jual)
		if len(data) > 9:
			sql += ",`barang_stok_toko`    = '{}',".format(barang_stok_toko)
			sql += "`barang_stok_gudang`   = '{}'".format(barang_stok_gudang)
			
		return connExecute(sql)

class BarangDataInterface(Resource):
	"""
		BarangInterface handling all data manipulation for data in `barang` table
		@route /master/barang - Get all data from the barang in form of array of JSON
		@route /master/barang/<string:id> - Get specific data from barang in form of object of JSON	
		@route /master/barang/create - Post data to here for input new data
	"""

	def get(self, id=False):

		barangController = BarangController()
		return barangController.get(id).form()
		
		sql  = "SELECT * FROM `barang` as a "
		sql += "INNER JOIN `kategori` as b "
		sql += "ON a.barang_kategori = b.kategori_id "
		sql += "INNER JOIN `merek` as c "
		sql += "ON a.barang_merek = c.merek_id "

		table_list = connExecute(sql);
		list_data  = []
		for data in table_list:
			table_data = Table(data['barang_id'])
			table_data.add_field_badge(data['kategori_nama'].title())
			table_data.add_field_text(data['barang_nama'].title() + " - " + data['barang_varian'])
			table_data.add_field_text(data['merek_nama'].title())
			table_data.add_field_price(data['barang_harga_jual'])
			table_data.add_field_text(str(data['barang_stok_toko']) + " / " + str(data['barang_stok_gudang']))
			list_data.append(table_data.get())
		return list_data

	def post(self):
		pass

class DataBarang(Resource):
	def get(self, id):
		sql  = "SELECT `barang_id`,`barang_satuan_grosir` as `barang_satuan`, "
		sql += "`barang_harga_beli` as `barang_harga` FROM `barang` WHERE `barang_id` = '{}'".format(id) 
		data = connExecute(sql)
		data = data[0]
		
		json_data = {
			'barang_id'     : data['barang_id'],
			'barang_satuan' : data['barang_satuan'],
			'barang_jumlah' : 0,
			'barang_harga'  : data['barang_harga'],
			'barang_total'  : 0,
		}

		return json_data