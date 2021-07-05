from Mappy.mysql import MysqlController, SQLBuilder
from Mappy.API.controller import Controller
from Master.components.controller_barang import ControllerBarang
from Master.models import Barang
from ..models import Order
from functions import Form, Options, generateId
from functions import Table

controller_barang = ControllerBarang()
class ControllerOrderPos(Controller):

	TABLE_NAME = "order"
	PRIMARY_KEY = "order_id"
	ORDER_TYPE = "21" # Order Type for Penjualan POS
	
	def __init__(self):
		""" Initialize controller super()
			[HOW_TO] super().__init__(MYSQL_TABLE_NAME, MYSQL_PRIMARY_KEY_FIELD_NAME) """
		super().__init__(self.TABLE_NAME, self.PRIMARY_KEY)

	def create(self, data):
		
		# Separate order_item from order_data
		order_item = data['order_item']
		data.__delitem__("order_item")
		fields = data

		# Make and Execute SQL
		sql = SQLBuilder().insert(self.TABLE_NAME).set(fields) \
			.on_duplicate_key(self.PRIMARY_KEY).update(fields) \
			.execute()
		
		# Delete all item inside and order
		SQLBuilder().delete(self.TABLE_NAME) \
					.where("order_id = data['order_id']") \
					.execute()

		# Re-add all the data to order_item
		for item in order_item:
			item['order_id'] = data['order_id']
			sql = SQLBuilder().insert("order_item").set(item) \
				.on_duplicate_key("order_item_id").update(item) \
				.execute()

			if data['order_status'] != "ST200":
				continue

			mysql_controller = MysqlController()
			order_posisi_stok = "barang_stok_" + data['order_posisi_stok']
			mysql_controller.set_sql("UPDATE `barang` SET `{}` = `{}` - {} WHERE `barang_id` = '{}'" \
				.format(order_posisi_stok, order_posisi_stok, item['barang_jumlah'], item['barang_id']))
			print(mysql_controller.execute())

		return sql

	def get(self, id=False):
		""" Get order data
			Input
				Id : ID can be provided to fetch specific order data
			Output
		"""

		orders = SQLBuilder().select("*", self.TABLE_NAME) \
				.inner_join("order_tipe").on("order_tipe = order_tipe_id") \
				.inner_join("order_status").on("order_status = order_status_id")

		# If ID Provided only fetch order with specific type and ID
		# If ID Not Provided fetch all order with specific type
		if id is not False:
			orders.where(f"order_id = '{id}' AND order_tipe = '{self.ORDER_TYPE}'")
		elif id is False:
			orders.where(f"order_tipe = '{self.ORDER_TYPE}'")

		# Execute SQL
		orders = orders.execute()

		# Fetch all item inside an order
		# order_item is table for getting order_item data
		for order in orders:

			# Make new array of order_item
			order['order_item'] = []
			order_item = SQLBuilder().select("*", "order_item") \
						.where("order_item.order_id = '{}'".format(order["order_id"])) \
						.execute()

			# Append every item inside `order_item`
			for item in order_item:
				order['order_item'].append(item)

		# Set the parent data to new model
		if id is not False and len(orders) > 0 :
			super().set(orders[0])
			return self

		super().set(orders)
		return self

	def form(self, loads=False):
		fields = ["order_id", "order_sales_id", "order_tipe", "order_item", \
				"order_tanggal", "order_tanggal_jatuh_tempo", "order_faktur", "order_posisi_stok", \
				"order_pajak", "order_diskon", "order_total", "order_sub_total", "order_status" ]
		order = Order(super().data()).get_and_distinct_keys(fields)
		order.get()["order_tipe"] = self.ORDER_TYPE

		sql = SQLBuilder().select("*", "barang") \
			.inner_join("kategori").on("barang_kategori = kategori_id") \
			.inner_join("merek").on("barang_merek = merek_id").where("barang_status = 1") \
			.execute()

		return {
			"order" : order.get(),
			"data_barang" : sql,
		}
