from Mappy.mysql import MysqlController, SQLBuilder
from Mappy.API.controller import Controller
from ..models import Pelanggan
from functions import Form, Options, generateId
from functions import Table

class ControllerPelanggan(Controller):

	TABLE_NAME = "master_pelanggan"
	PRIMARY_KEY = "pelanggan_id"

	def __init__(self):
		""" Initialize controller super()
			[HOW_TO] super().__init__(MYSQL_TABLE_NAME, MYSQL_PRIMARY_KEY_FIELD_NAME) """
		super().__init__(self.TABLE_NAME, self.PRIMARY_KEY)

	def create(self, data):
		""" Function for adding or edit existing data in MySQL Database """

		# Load data from Mappy Form Format
		fields = Form().load(data).unpack()

		# Make and Execute SQL
		sql = SQLBuilder()
		sql.insert(self.TABLE_NAME).set(fields).on_duplicate_key(self.PRIMARY_KEY).update(fields)
		super().query(sql.build())
		return super().data()

	def form(self, loads = False):

		pelanggan_data = super().data()

		# Make new "Pelanggan" instance
		pelanggan = Pelanggan() if isinstance(pelanggan_data, list) else Pelanggan(pelanggan_data)
		data = pelanggan.data()

		# Make new Form Instance
		# Forms should be in order
		form = Form()
		form.key(self.PRIMARY_KEY).set_primary_key(data[self.PRIMARY_KEY])
		form.key("pelanggan_nama").text("Nama Pelanggan", "Masukan Nama Pelanggan", data["pelanggan_nama"])
		form.key("pelanggan_alamat").text("Alamat Pelanggan", "Masukan Alamat Pelanggan", data["pelanggan_alamat"])
		form.key("pelanggan_kontak").text("Kontak", "Masukan Kontak Pelanggan", data["pelanggan_kontak"])
		return form.get()

	def table(self, loads=False):
		""" Function for converting raw data to Mappy Table Format """

		sql = SQLBuilder().select("*", self.TABLE_NAME)
		super().query(sql.build())

		table = Table()
		for data in super().data():
			row = table.Row()
			row.set_primary_key(data['pelanggan_id'])
			row.text(data['pelanggan_nama'].title())
			row.text(data['pelanggan_alamat'])
			row.text(data['pelanggan_kontak'].title())
			table.commit_row(row)
		return table.data()

	def table_with_state(self):
		return []