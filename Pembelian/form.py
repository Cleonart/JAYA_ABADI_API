from flask_restful import Resource,request
from mysql import connExecute
import random
from Universal.options import opt
from Universal.form import form
from Universal.table import tbl

class FormPembelian(Resource):

	def get(self):
		json_data = {}

		json_data['data_supplier'] = {}
		temporary_data = connExecute("SELECT * FROM `master_supplier`")
		for data in temporary_data:
			json_data['data_supplier'][data['supplier_id']] = "{}".format(data['supplier_nama'])

		data_product_sql = ""
		data_product_sql += "SELECT `barang_id`,`barang_nama`,`merek_nama`,`kategori_nama`,`barang_varian` FROM `barang` as a "
		data_product_sql += "INNER JOIN `merek` as b "
		data_product_sql += "ON `barang_merek` = `merek_id` "
		data_product_sql += "INNER JOIN `kategori` as c "
		data_product_sql += "ON `barang_kategori` = `kategori_id`"
		temporary_data = connExecute(data_product_sql)

		json_data['data_product'] = {}
		for data in temporary_data:
			json_data['data_product'][data['barang_id']] = "[{}] {} - {} {}".format(data['kategori_nama'],data['merek_nama'],data['barang_nama'],data['barang_varian'])
		
		temporary_data = connExecute("SELECT * FROM `satuan`")
		json_data['data_satuan']  = {}
		for data in temporary_data:
			json_data['data_satuan'][data['satuan_id']] = "{}".format(data['satuan_nama'])	

		return json_data

	def post(self):
		data = request.get_json()
		pembelian_id                  = data['pembelian_id']

		if(pembelian_id == ""):
			pembelian_id   = "INV" + str(random.randint(100000,999999))

		pembelian_supplier_id         = data['pembelian_supplier_id']
		pembelian_tanggal             = data['pembelian_tanggal']
		pembelian_tanggal_jatuh_tempo = data['pembelian_tanggal_jatuh_tempo']
		pembelian_item                = data['pembelian_item']
		pembelian_faktur              = int(0)
		pembelian_pajak               = int(0)
		pembelian_diskon              = int(data['pembelian_diskon'])
		pembelian_total               = int(data['pembelian_total'])
		pembelian_status              = data['pembelian_status']; 

		sql  = "INSERT INTO `pembelian` SET "
		sql += "`pembelian_id`                   = '{}',".format(pembelian_id)
		sql += "`pembelian_supplier_id`          = '{}',".format(pembelian_supplier_id)
		sql += "`pembelian_tanggal`              = '{}',".format(pembelian_tanggal)
		sql += "`pembelian_tanggal_jatuh_tempo`  = '{}',".format(pembelian_tanggal_jatuh_tempo)
		sql += "`pembelian_faktur`               = '{}',".format(pembelian_faktur)
		sql += "`pembelian_pajak`                = '{}',".format(pembelian_pajak)
		sql += "`pembelian_diskon`               = '{}',".format(pembelian_diskon)
		sql += "`pembelian_total`                = '{}',".format(pembelian_total)
		sql += "`pembelian_status`               = '{}'".format(pembelian_status)
		sql += "ON DUPLICATE KEY UPDATE "
		sql += "`pembelian_supplier_id`          = '{}',".format(pembelian_supplier_id)
		sql += "`pembelian_tanggal`              = '{}',".format(pembelian_tanggal)
		sql += "`pembelian_tanggal_jatuh_tempo`  = '{}',".format(pembelian_tanggal_jatuh_tempo)
		sql += "`pembelian_faktur`               = '{}',".format(pembelian_faktur)
		sql += "`pembelian_pajak`                = '{}',".format(pembelian_pajak)
		sql += "`pembelian_diskon`               = '{}',".format(pembelian_diskon)
		sql += "`pembelian_total`                = '{}',".format(pembelian_total)
		sql += "`pembelian_status`               = '{}'".format(pembelian_status)
		execs = connExecute(sql)
		return execs

class TabelPembelian(Resource):

	def get(self):

		json_data = {}
		data_product_sql = ""
		data_product_sql += "SELECT * FROM `pembelian` as a "
		data_product_sql += "INNER JOIN `pembelian_status` as b ON a.pembelian_status = b.pembelian_status_id "
		data_product_sql += "INNER JOIN `master_supplier` as c ON a.pembelian_supplier_id = c.supplier_id"
		
		json_data['pembelian_data'] = connExecute(data_product_sql)
		json_data['pembelian_belum_dibayar'] = 0
		json_data['pembelian_jatuh_tempo']   = 0
		json_data['pembelian_selesai']       = 0
		
		list_data  = []
		for pembelian in json_data['pembelian_data']:
			
			table_data = tbl(pembelian['pembelian_id'])
			table_data.add_field_text(pembelian['supplier_nama'].title())
			table_data.add_field_text(pembelian['pembelian_tanggal'].title())
			table_data.add_field_text(pembelian['pembelian_tanggal_jatuh_tempo'].title())
			
			# Pembelian yang belum dibayar
			if pembelian['pembelian_status'] == 'ST202':
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