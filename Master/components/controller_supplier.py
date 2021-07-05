from Mappy.mysql import MysqlController, SQLBuilder
from Mappy.API.controller import Controller
from ..models import Supplier
from functions import Form, Options, generateId
from functions import Table

class ControllerSupplier(Controller):

	TABLE_NAME = "master_supplier"
	PRIMARY_KEY = "supplier_id"

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
		sql = sql.insert(self.TABLE_NAME).set(fields) \
				.on_duplicate_key(self.PRIMARY_KEY) \
				.update(fields).build()
		super().query(sql)
		return super().data()

	def form(self, loads = False):

		# Make new "Supplier" instance
		supplier = Supplier() if isinstance(super().data(), list) \
							  else Supplier(super().data())
		data = supplier.data()

		# Make new Form Instance
		# Forms should be in order
		form = Form()
		form.key(self.PRIMARY_KEY).set_primary_key(data[self.PRIMARY_KEY])
		form.key("supplier_nama").text("Nama Supplier", "Masukan Nama Supplier", data["supplier_nama"].upper())
		form.key("supplier_alamat").text("Alamat Supplier", "Masukan Nama Supplier", data["supplier_alamat"])
		form.key("supplier_provinsi").select("Provinsi Supplier", "Silahkan pilih provinsi", Options.provinsi(), data["supplier_provinsi"])
		form.key("supplier_kota").select("Kota Supplier", "Silahkan pilih kota", Options.kota(), data["supplier_kota"])
		form.key("supplier_telepon").text("No. Telepon", "Masukan Nomor Telepon", data["supplier_telepon"])

		return form.get()

	def table(self, loads=False):
		""" Function for converting raw data to Mappy Table Format """

		sql = SQLBuilder().select("*", self.TABLE_NAME)
		super().query(sql.build())

		table = Table()
		for data in super().data():
			row = table.Row()
			row.set_primary_key(data['supplier_id'])
			row.text(data['supplier_nama'].title())
			row.text(data['supplier_alamat'])
			row.text(data['supplier_provinsi'] + "/" + data['supplier_kota'])
			row.text(data['supplier_telepon'])
			table.commit_row(row)
		return table.data()

	def table_with_state(self):
		return []