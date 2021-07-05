from Mappy.mysql import MysqlController, SQLBuilder
from Mappy.API.controller import Controller
from ..models import Pengguna
from functions import Form, Options, generateId
from functions import Table

class ControllerPengguna(Controller):

	TABLE_NAME = "pengguna"
	PRIMARY_KEY = "pengguna_id"

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

		pengguna_data = super().data()

		# Make new "Pelanggan" instance
		pengguna = Pengguna() if isinstance(pengguna_data, list) else Pengguna(pengguna_data)
		data = pengguna.data()

		# Make new Form Instance
		# Forms should be in order
		form = Form()
		form.key(self.PRIMARY_KEY).set_primary_key(data[self.PRIMARY_KEY])
		form.key("pengguna_nama").text("Nama Pengguna", "Masukan Nama Pengguna", data["pengguna_nama"])
		form.key("pengguna_posisi").select("Pilih Posisi Pengguna", "Posisi Pengguna", Options.posisi(), data["pengguna_posisi"])
		form.key("pengguna_status").select("Pilih Status Pengguna", "Pilih Status Pengguna", Options.status(), data["pengguna_status"])
		return form.get()

	def table(self, loads=False):
		""" Function for converting raw data to Mappy Table Format """

		sql = SQLBuilder().select("*", self.TABLE_NAME) \
						  .inner_join("posisi").on("posisi.`posisi_id` = pengguna.`pengguna_posisi`")
		super().query(sql.build())

		table = Table()
		for data in super().data():
			row = table.Row()
			row.set_primary_key(data['pengguna_id'])
			row.text(data['pengguna_nama'].title())
			row.text(data['posisi_nama'])
			row.text(data['pengguna_status'])
			table.commit_row(row)
		return table.data()

	def table_with_state(self):
		return []