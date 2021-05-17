from functions import Options, Table, generateId
from flask_restful import Resource,request
from mysql import connExecute
from datetime import date
from Universal.form import form
from Universal.table import tbl

class Order(Resource):
	""" Class [Order]
		^ Function Mapping
		
		* /orders/<string:type> 
		Mengambil semua order yang terdaftar baik PENJUALAN atau PEMBELIAN

		* /order/<string:id>
		
		Kelas untuk menangani masalah order
		adapun [Order] digunakan oleh
	"""

	orderTypeMap = {
		"penjualan" : 200,
		"pembelian" : 100
	}

	def get(self, type=None, id=None):
		if id == None:
			return self.getOrders(self.orderTypeMap[type])
		return self.getOrder(id)

	def post(self, id=None):
		data = request.get_json()
		self.createOrder(data)

	""" Get all orders """
	def listOfOrder(self):
		return "data order semua"

	"""
		Create order for pembelian and penjualan 
		Order have 2 types [PEMBELIAN] with code 100 and [PENJUALAN] with code 200
	"""
	def createOrder(self, data):
		pembelian_id = data['pembelian_id']

		if pembelian_id == "":
			pembelian_id = generateId("INV")

		order_type                    = data['order_type']
		order_sales_id                = data['order_sales_id']
		order_customer_id             = data['order_customer_id']
		pembelian_supplier_id         = data['pembelian_supplier_id']
		pembelian_tanggal             = data['pembelian_tanggal']
		pembelian_tanggal_jatuh_tempo = data['pembelian_tanggal_jatuh_tempo']
		pembelian_item                = data['pembelian_item']
		pembelian_faktur              = int(0)
		pembelian_pajak               = int(0)
		pembelian_diskon              = int(data['pembelian_diskon'])
		pembelian_total               = int(data['pembelian_total'])
		pembelian_status              = data['pembelian_status']; 
		
		# Switch between [PEMBELIAN] and [PENJUALAN]
		operator     = '+'  # Default operator for product processing is addition
		if order_type == 200:
			operator = '-'

		sql  = "INSERT INTO `order` SET "
		sql += "`pembelian_id`                   = '{}',".format(pembelian_id)
		sql += "`order_type`                     = '{}',".format(order_type)
		sql += "`order_sales_id`                 = '{}',".format(order_sales_id)
		sql += "`order_customer_id`              = '{}',".format(order_customer_id)
		sql += "`pembelian_supplier_id`          = '{}',".format(pembelian_supplier_id)
		sql += "`pembelian_tanggal`              = '{}',".format(pembelian_tanggal)
		sql += "`pembelian_tanggal_jatuh_tempo`  = '{}',".format(pembelian_tanggal_jatuh_tempo)
		sql += "`pembelian_faktur`               = '{}',".format(pembelian_faktur)
		sql += "`pembelian_pajak`                = '{}',".format(pembelian_pajak)
		sql += "`pembelian_diskon`               = '{}',".format(pembelian_diskon)
		sql += "`pembelian_total`                = '{}',".format(pembelian_total)
		sql += "`pembelian_status`               = '{}'".format(pembelian_status)
		sql += "ON DUPLICATE KEY UPDATE "
		sql += "`order_type`                     = '{}',".format(order_type)
		sql += "`order_sales_id`                 = '{}',".format(order_sales_id)
		sql += "`order_customer_id`              = '{}',".format(order_customer_id)
		sql += "`pembelian_supplier_id`          = '{}',".format(pembelian_supplier_id)
		sql += "`pembelian_tanggal`              = '{}',".format(pembelian_tanggal)
		sql += "`pembelian_tanggal_jatuh_tempo`  = '{}',".format(pembelian_tanggal_jatuh_tempo)
		sql += "`pembelian_faktur`               = '{}',".format(pembelian_faktur)
		sql += "`pembelian_pajak`                = '{}',".format(pembelian_pajak)
		sql += "`pembelian_diskon`               = '{}',".format(pembelian_diskon)
		sql += "`pembelian_total`                = '{}',".format(pembelian_total)
		sql += "`pembelian_status`               = '{}'".format(pembelian_status)
		execs = connExecute(sql)

		# Register the transaction
		if pembelian_status == "ST200":
			transactionId = generateId("TRC")
			sql  = "INSERT INTO `transaksi` "
			sql += "(`transaksi_id`, `order_id`, `transaksi_jumlah`) "
			sql += "VALUES ('{}', '{}', '{}'); ".format(transactionId, pembelian_id, pembelian_total)
			connExecute(sql)

		# Delete all previous item
		sql = "DELETE FROM `order_item` WHERE `pembelian_id` = '{}'".format(pembelian_id)
		connExecute(sql)

		# Registering all item
		for item in pembelian_item:
			sql  = "INSERT INTO `order_item` "
			sql += "(`pembelian_id`, `barang_id`, `barang_satuan`, "
			sql += "`barang_jumlah`, `barang_harga`, `barang_total`) "
			sql += "VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(pembelian_id, item['barang_id'], item['barang_satuan'], int(item['barang_jumlah']), int(item['barang_harga']), int(item['barang_total']))
			connExecute(sql)

			# Update the barang_total to the database
			if pembelian_status == "ST200":
				sql  = "UPDATE `barang` "
				sql += "SET `barang_stok_toko` = `barang_stok_toko` {} '{}' ".format(operator, item['barang_jumlah'])
				sql += "WHERE `barang`.`barang_id` = '{}' ".format(item['barang_id'])
				connExecute(sql)

		return execs

	def getOrder(self, id):
		json_data = {}
		json_data['data_supplier']  = Options.objectDataSupplier()
		json_data['data_pelanggan'] = Options.objectDataPelanggan()
		json_data['data_pengguna']  = Options.objectDataPengguna(3001)
		json_data['data_product']   = Options.objectDataBarang()
		json_data['data_satuan']    = Options.objectDataSatuan()

		# Get Order Data if exist
		if id[0:3] == "INV":
			sql = "SELECT * FROM `order` WHERE `pembelian_id` = '{}' ".format(id)
			order_data = connExecute(sql)[0]

			sql = "SELECT * FROM `order_item` WHERE `pembelian_id` = '{}'".format(id)
			order_item = connExecute(sql)
			order_data['pembelian_item'] = order_item
			json_data['data_order'] = order_data

		return json_data

	def getOrders(self, type):

		json_data = {}
		data_product_sql = ""
		data_product_sql += "SELECT * FROM `order` as a "
		data_product_sql += "INNER JOIN `pembelian_status` as b ON a.pembelian_status = b.pembelian_status_id "
		
		if type == 100:
			data_product_sql += "INNER JOIN `master_supplier` as c ON a.pembelian_supplier_id = c.supplier_id "
		
		elif type == 200:
			data_product_sql += "INNER JOIN `master_pelanggan` as c ON a.order_customer_id = c.pelanggan_id "
			data_product_sql += "INNER JOIN `pengguna` as d ON a.order_sales_id = d.pengguna_id "

		data_product_sql += "WHERE `order_type` =  '{}' ".format(type)

		json_data['pembelian_data']          = connExecute(data_product_sql)
		json_data['pembelian_belum_dibayar'] = 0
		json_data['pembelian_jatuh_tempo']   = 0
		json_data['pembelian_selesai']       = 0
		
		list_data  = []
		for pembelian in json_data['pembelian_data']:
			
			table_data = tbl(pembelian['pembelian_id'])
			
			if type == 100:
				table_data.add_field_text(pembelian['supplier_nama'].title())

			elif type == 200:
				table_data.add_field_text(pembelian['pengguna_nama'].title())
				table_data.add_field_text(pembelian['pelanggan_nama'].title())

			table_data.add_field_text(pembelian['pembelian_tanggal'] + ' / ' + pembelian['pembelian_tanggal_jatuh_tempo'])
			
			# Jatuh Tempo
			if pembelian['pembelian_tanggal_jatuh_tempo'] == str(date.today()) and pembelian['pembelian_status'] != 'ST200':
				table_data.add_field_badge_warning("JATUH TEMPO".title())
				json_data['pembelian_jatuh_tempo'] += pembelian['pembelian_total']

			# Pembelian yang belum dibayar
			elif pembelian['pembelian_status'] == 'ST202':
				table_data.add_field_badge_danger(pembelian['pembelian_status_nama'].title())
				json_data['pembelian_belum_dibayar'] += pembelian['pembelian_total']

			# Pembelian yang selesai
			elif pembelian['pembelian_status'] == 'ST200':
				table_data.add_field_badge(pembelian['pembelian_status_nama'].title())
				json_data['pembelian_selesai'] += pembelian['pembelian_total']

			table_data.add_field_price(pembelian['pembelian_total'])
			list_data.append(table_data.get())

		json_data['pembelian_data'] = list_data
		return json_data
