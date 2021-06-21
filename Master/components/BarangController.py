from mysql import MysqlController
from flask import abort
from .Controller import Controller
from functions import Form, Options, Table, generateId
from ..models import Barang

class BarangController(Controller):

	MYSQL_TABLE_NAME = "barang"
	MYSQL_PRIMARY_KEY_FIELD_NAME = "barang_id"

	def __init__(self):
		""" 
			Initialize controller super()
			[HOW_TO] super().__init__(MYSQL_TABLE_NAME, MYSQL_PRIMARY_KEY_FIELD_NAME)
		"""
		super().__init__(self.MYSQL_TABLE_NAME, self.MYSQL_PRIMARY_KEY_FIELD_NAME)

	def create(self):
		""" Function for adding or edit existing data in MySQL Database """
		pass

	def form(self):
		""" Extract data from get() function to compatible Mappy Form Format """
		if(super().is_data_valid()):
			if type(super().__dict__['internal_data']) is list:
				self.ERROR['msg'] = "Form data should be object of JSON for mappy"
				self.ERROR['code'] = "INVALID_DATA_TYPE"
				self.ERROR['success'] = False
				return self.ERROR

			# Make new Barang Instance
			barang = Barang(super().__dict__['internal_data'])
			barang_data = barang.__dict__

			# Make new Form Instance
			# Forms should be in order
			form_barang = Form(barang_data['barang_id'])
			form_barang.add_text("Nama Barang", "Masukan Nama Barang", barang_data['barang_nama'])
			form_barang.add_select("Kategori", "Masukan Kategori", Options.kategori(), barang_data['barang_kategori'])
			form_barang.add_select("Merek", "Masukan Nama Merek", Options.merek(), barang_data['barang_merek'])
			form_barang.add_text("Varian Barang", "Masukan Varian Barang", barang_data['barang_varian'])
			form_barang.add_select("Satuan Eceran", "Satuan Eceran Barang", Options.satuan(), barang_data['barang_satuan_eceran'])
			form_barang.add_select("Satuan Grosir", "Satuan Grosir Barang", Options.satuan(), barang_data['barang_satuan_grosir'])
			form_barang.add_text("Harga Beli", "Masukan Harga Beli", barang_data['barang_harga_beli'])
			form_barang.add_text("Harga Jual", "Masukan Harga Jual", barang_data['barang_harga_jual'])

			# Stok awal toko and stok awal gudang is one time data
			# Only inputted for the first time, and didn't show up when updating data
			if super().is_data_exists():
				form_barang.add_text("Stok Awal Toko", "Masukan Stok Awal", 0)
				form_barang.add_text("Stok Awal Gudang", "Masukan Stok Awal Gudang", 0)

			return form_barang.get()