from Mappy.mysql import MysqlController, SQLBuilder
from Mappy.API.controller import Controller
from ..models import Perusahaan
from functions import Form, Options, generateId
from functions import Table

class ControllerPerusahaan(Controller):

	TABLE_NAME = "master_perusahaan"
	PRIMARY_KEY = "perusahaan_id"

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

		perusahaan_data = super().data()

		# Make new "Perusahaan" instance
		perusahaan = Perusahaan() if isinstance(perusahaan_data, list) else Perusahaan(perusahaan_data)
		data = perusahaan.data()

		# Make new Form Instance
		# Forms should be in order
		form = Form()
		form.key(self.PRIMARY_KEY).set_primary_key(data[self.PRIMARY_KEY])
		form.key("perusahaan_nama").text("Nama Perusahaan", "Masukan Nama Perusahaan", data["perusahaan_nama"])
		form.key("perusahaan_alamat").text("Alamat Perusahaan", "Masukan Alamat Perusahaan", data["perusahaan_alamat"])
		form.key("perusahaan_kontak").text("Kontak Perusahaan", "Masukan Kontak Perusahaan", data["perusahaan_kontak"])
		form.key("perusahaan_npwp").text("NPWP Perusahaan", "Masukan NPWP Perusahaan", data["perusahaan_npwp"])
		return form.get()