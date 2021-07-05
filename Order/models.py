from functions import Options
from functions import generateId

class Master():

	def get(self, keysToGet=[]):

		# Load without distinct key
		if len(keysToGet) == 0:
			return self.__dict__

		# Load and distinct key
		return self.distinctKeys(keysToGet)
	
	def data(self):
		return self.__dict__

	def load(self, load_file):
		self.__dict__ = load_file
		return self

	### Soon end of support ###
	def distinctKeys(self, keysToGet=[]):
		arrayData = {}
		selfData = self.__dict__
		for key in selfData.keys():
			if key in keysToGet:
				arrayData[key] = selfData[key]
		self.__dict__ = arrayData
		return self
	### Soon end of support ###

	def get_and_distinct_keys(self, keys=[]):
		distincted_keys = {}
		for key in self.__dict__.keys():
			if key in keys:
				distincted_keys[key] = self.__dict__[key]
		self.__dict__ = distincted_keys
		return self

class Order(Master):

	def __init__(self, loads=False):
		self.order_id = generateId("INV")
		self.order_supplier_id = ""
		self.order_pelanggan_id = ""
		self.order_sales_id = ""
		self.order_tipe = 0
		self.order_tanggal = ""
		self.order_tanggal_jatuh_tempo = ""
		self.order_item = []
		self.order_faktur = 0
		self.order_pajak = 0
		self.order_diskon = 0
		self.order_total = 0
		self.order_sub_total = 0
		self.order_status = ""
		self.order_posisi_stok = ""

		if loads:
			self.__dict__ = loads

class OrderGetter():

	def __init__(self, loads=False):
		self.data_supplier = Options.objectDataSupplier()
		self.data_pelanggan = Options.objectDataPelanggan()
		self.data_pengguna = Options.objectDataPengguna(3001)
		self.data_barang = Options.objectDataBarang()
		self.data_satuan = Options.objectDataSatuan()