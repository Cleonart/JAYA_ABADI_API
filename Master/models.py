from functions import generateId

class Master():

	def get(self, keysToGet=[]):

		# Load without distinct key
		if len(keysToGet) == 0:
			return self.__dict__

		# Load and distinct key
		return self.distinctKeys(keysToGet)
	
	def dict(self):
		return self.__dict__

	def load(self, load_file):
		self.__dict__ = load_file
		return self

	def distinctKeys(self, keysToGet=[]):
		arrayData = {}
		selfData = self.__dict__
		for key in selfData.keys():
			if key in keysToGet:
				arrayData[key] = selfData[key]
		self.__dict__ = arrayData
		return self

class Barang(Master):

	barang_id = generateId("B")
	barang_nama = ""
	barang_kategori = ""
	barang_merek = ""
	barang_varian = ""
	barang_satuan_eceran = ""
	barang_satuan_grosir = ""
	barang_harga_beli = ""
	barang_harga_jual = ""

	def __init__(self, loads=False):
		self.barang_id = generateId("B")
		self.barang_nama = ""
		self.barang_kategori = ""
		self.barang_merek = ""
		self.barang_varian = ""
		self.barang_satuan_eceran = ""
		self.barang_satuan_grosir = ""
		self.barang_harga_beli = ""
		self.barang_harga_jual = ""

		if loads:
			self.load(loads)
