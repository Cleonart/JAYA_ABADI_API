from Mappy.mysql import MysqlController, SQLBuilder
from Mappy.API.controller import Controller
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

	def create(self, data):
		""" Function for adding or edit existing data in MySQL Database """

		# Load data from Mappy Form Format
		fields = Form().load(data).unpack()

		# Make and Execute SQL
		sql = SQLBuilder()
		sql.insert("barang").set(fields).on_duplicate_key("barang_id").update(fields)
		super().query(sql.build())
		return super().data()

	def form(self, loads=False):
		""" 
			Extract data from get() function and convert it 
			to compatible Mappy Form Format
		"""

		barang_data = super().data()

		# Make new Barang Instance
		barang = Barang() if isinstance(barang_data, list) else Barang(barang_data)
		data = barang.data()

		# Make new Form Instance
		# Forms should be in order
		form = Form()
		form.key("barang_id").set_primary_key(data['barang_id'])
		form.key("barang_nama").text("Nama Barang", "Masukan Nama Barang", data['barang_nama'].upper())
		form.key("barang_kategori").select("Kategori", "Masukan Kategori", Options.kategori(), data['barang_kategori'])
		form.key("barang_merek").select("Merek", "Masukan Nama Merek", Options.merek(), data['barang_merek'])
		form.key("barang_varian").text("Varian Barang", "Masukan Varian Barang", data['barang_varian'])
		form.key("barang_satuan_eceran").select("Satuan Eceran", "Satuan Eceran Barang", Options.satuan(), data['barang_satuan_eceran'])
		form.key("barang_satuan_grosir").select("Satuan Grosir", "Satuan Grosir Barang", Options.satuan(), data['barang_satuan_grosir'])
		form.key("barang_harga_beli").text("Harga Beli", "Masukan Harga Beli", data['barang_harga_beli'])
		form.key("barang_harga_jual").text("Harga Jual", "Masukan Harga Jual", data['barang_harga_jual'])

		# Stok awal toko and stok awal gudang is one time data
		# Only inputted for the first time, and didn't show up when updating data
		if not super().is_data_exists() or isinstance(barang_data, list):
			form.key("barang_stok_toko").text("Stok Awal Toko", "Masukan Stok Awal", 0)
			form.key("barang_stok_gudang").text("Stok Awal Gudang", "Masukan Stok Awal Gudang", 0)

		return form.get()

	def table(self, loads=False):
		""" Function for converting raw data to Mappy Table Format """

		sql = SQLBuilder().select("*", "barang") \
			.inner_join("kategori").on("`barang`.barang_kategori = `kategori`.kategori_id") \
			.inner_join("merek").on("`barang`.barang_merek = `merek`.merek_id") \
			.where("barang.barang_status = 1")

		super().query(sql.build())
		table = Table()
		for data in super().data():
			row = table.Row()
			row.set_primary_key(data['barang_id'])
			row.badge(data['kategori_nama'].title())
			row.text(f"{data['merek_nama'].title()} - {data['barang_nama'].title()} - {data['barang_varian']}")
			row.price(data['barang_harga_jual'])
			row.text(f"{str(data['barang_stok_toko'])} / {str(data['barang_stok_gudang'])}")
			table.commit_row(row)
			row = table.Row()
		return table.data()

	def table_with_state(self, state):
		states = {'active' : 1, 'inactive' : 0}

		sql = SQLBuilder().select("*", "barang") \
			.inner_join("kategori").on("`barang`.barang_kategori = `kategori`.kategori_id") \
			.inner_join("merek").on("`barang`.barang_merek = `merek`.merek_id") \
			.where(f"barang.barang_status = {states[state]}")

		return super().query(sql.build()).data()
