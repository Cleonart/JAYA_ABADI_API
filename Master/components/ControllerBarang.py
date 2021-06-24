from mysql import MysqlController
from .controller import Controller
from ..models import Barang
from functions import Form, Options, generateId
from functions import Table

class ControllerBarang(Controller):

	MYSQL_TABLE_NAME = "barang"
	MYSQL_PRIMARY_KEY_FIELD_NAME = "barang_id"

	def __init__(self):
		""" Initialize controller super()
			[HOW_TO] super().__init__(MYSQL_TABLE_NAME, MYSQL_PRIMARY_KEY_FIELD_NAME) """
		super().__init__(self.MYSQL_TABLE_NAME, self.MYSQL_PRIMARY_KEY_FIELD_NAME)

	def create(self):
		""" Function for adding or edit existing data in MySQL Database """

		sql = self.sqlbuilder()
		fields = {
			"barang_id" : "123",
			"barang_nama" : "tes",
			"barang_kategori" : "tes",
			"barang_varian" : "te",
			"barang_merek" : "ts",
			"barang_satuan_eceran" : "t",
			"barang_satuan_grosir" : "t",
			"barang_harga_beli" : 2000,
			"barang_harga_jual" : 5000
		}
		if True:
			fields['barang_stok_toko'] = 0
			fields['barang_stok_gudang'] = 0

		sql.insert("barang").set(fields).on_duplicate_key("barang_id").update(fields)
		super().query(sql.build())
		return super().data()

	def form(self, loads=False):
		""" 
			Extract data from get() function and convert it 
			to compatible Mappy Form Format
		"""
		if(super().is_data_exists):
			
			barang_data = super().data()

			# Make new Barang Instance
			barang = Barang() if isinstance(barang_data, list) else Barang(barang_data)
			barang_data = barang.data()

			# Make new Form Instance
			# Forms should be in order
			form_barang = Form()
			form_barang.set_primary_key(barang_data['barang_id'])
			form_barang.text("Nama Barang", "Masukan Nama Barang", barang_data['barang_nama'])
			form_barang.select("Kategori", "Masukan Kategori", Options.kategori(), barang_data['barang_kategori'])
			form_barang.select("Merek", "Masukan Nama Merek", Options.merek(), barang_data['barang_merek'])
			form_barang.text("Varian Barang", "Masukan Varian Barang", barang_data['barang_varian'])
			form_barang.select("Satuan Eceran", "Satuan Eceran Barang", Options.satuan(), barang_data['barang_satuan_eceran'])
			form_barang.select("Satuan Grosir", "Satuan Grosir Barang", Options.satuan(), barang_data['barang_satuan_grosir'])
			form_barang.text("Harga Beli", "Masukan Harga Beli", barang_data['barang_harga_beli'])
			form_barang.text("Harga Jual", "Masukan Harga Jual", barang_data['barang_harga_jual'])

			# Stok awal toko and stok awal gudang is one time data
			# Only inputted for the first time, and didn't show up when updating data
			if super().is_data_exists():
				form_barang.text("Stok Awal Toko", "Masukan Stok Awal", 0)
				form_barang.text("Stok Awal Gudang", "Masukan Stok Awal Gudang", 0)

			return form_barang.get()

	def table(self, loads=False):
		""" Function for converting raw data to Mappy Table Format """

		sql  = "SELECT * FROM `barang` "
		sql += "INNER JOIN `kategori` "
		sql += "ON `barang`.barang_kategori = `kategori`.kategori_id "
		sql += "INNER JOIN `merek` "
		sql += "ON `barang`.barang_merek = `merek`.merek_id "
		super().query(sql)

		table = Table()
		for data in super().data():
			row = table.Row()
			row.set_primary_key(data['barang_id'])
			row.badge(data['kategori_nama'].title())
			row.text(data['barang_nama'].title() + " - " + data['barang_varian'])
			row.text(data['merek_nama'].title())
			row.price(data['barang_harga_jual'])
			row.text(str(data['barang_stok_toko']) + " / " + str(data['barang_stok_gudang']))
			table.commit_row(row)
		return table.data()

	def table_with_state(self, state):
		states = {'active' : 1, 'inactive' : 0}
		sql = self.sqlbuilder()
		sql.select("*", "barang").where(f"`barang_status` = {states[state]}")
		return super().query(sql.build()).data()

	class sqlbuilder():
		"""
			When set, id must be at the
		"""

		key = None
		sql = ""

		def __init__(self):
			self.sql = ""

		def __repr__(self):
			return str(self.sql)

		def insert(self, table_name):
			self.sql = f"INSERT INTO `{table_name}` "
			return self	

		def select(self, _field, _from):
			self.sql = f"SELECT {_field} FROM `{_from}` "
			return self

		def where(self, condition):
			self.sql += "WHERE {} ".format(condition)
			return self

		def set(self, field):
			self.sql += "SET "
			fields = []
			for key in list(field.keys()):
				fields.append(f"`{key}` = '{field[key]}'")
			self.sql += ",".join(fields) + " "
			return self

		def on_duplicate_key(self, key):
			self.sql += "ON DUPLICATE KEY "
			self.key = key
			return self

		def update(self, field):
			self.sql += "UPDATE "
			fields = []
			if self.key != None:
				for key in list(field.keys()):
					if key != self.key:
						fields.append(f"`{key}` = '{field[key]}'")
				self.sql += ",".join(fields)
			return self

		def build(self):
			return self.sql