from flask_restful import Resource,request
from mysql import connExecute

class Barang(Resource):

	tableName = "barang"
	
	def get(self, id=None, onlyActive=None):
		print(id, onlyActive)
		"""
			Mengambil barang dari database
			id = None; mengambil semua data
			id != None; Mengambil barang tertentu 
		"""
		if id == None:

			# Mengambil semua data yang diarsipkan
			if onlyActive == 'inactive': 
				return connExecute("SELECT * FROM `{}` WHERE `barang_status` = 0".format(self.tableName))

			# Mengambil semua data yang tidak diarsipkan
			elif onlyActive == 'active': 
				return connExecute("SELECT * FROM `{}` WHERE `barang_status` = 1".format(self.tableName))

			# Mengambil semua data
			return connExecute("SELECT * FROM `{}`".format(self.tableName))

		# Mengambil data berdasarkan ID
		return connExecute("SELECT * FROM `{}`".format(self.tableName))[0]

	def post(self,id=None):
		pass
	
	def delete(self,id=None):
		"""
			Menghapus data barang spesifik dari database
		"""
		connExecute("UPDATE `{}` SET `barang_status` = 0 WHERE `barang_id` = '{}'".format(self.tableName, id))
		return {'valid' : True, 'msg' : "Data successfully archived"}

	def getWithTableFormat(self):
		sql  = "SELECT * FROM `barang` as a "
		sql += "INNER JOIN `kategori` as b "
		sql += "ON a.barang_kategori = b.kategori_id "
		sql += "INNER JOIN `merek` as c "
		sql += "ON a.barang_merek = c.merek_id "
		sql += "WHERE `barang_status` = 1"

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