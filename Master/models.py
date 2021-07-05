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

class Barang(Master):

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
		self.barang_stok_toko = ""
		self.barang_stok_gudang = ""
		
		if loads:
			self.load(loads)

class Pelanggan(Master):

	def __init__(self, loads=False):
		self.pelanggan_id = generateId("PEL")
		self.pelanggan_nama = ""
		self.pelanggan_alamat = ""
		self.pelanggan_kontak = ""

		if loads:
			self.load(loads)

class Pengguna(Master):
	
	def __init__(self, loads=False):
		self.pengguna_id = generateId("USR")
		self.pengguna_nama = ""
		self.pengguna_posisi = ""
		self.pengguna_status = ""

		if loads:
			self.load(loads)

class Supplier(Master):

	def __init__(self, loads=False):
		self.supplier_id = generateId("USR")
		self.supplier_nama = ""
		self.supplier_alamat = ""
		self.supplier_provinsi = ""
		self.supplier_kota = ""
		self.supplier_telepon = ""

		if loads:
			self.load(loads)

class Perusahaan(Master):

	def __init__(self, loads=False):
		self.perusahaan_id = generateId("ENT")
		self.perusahaan_nama = ""
		self.perusahaan_alamat = ""
		self.perusahaan_kontak = ""
		self.perusahaan_npwp = ""

		if loads:
			self.load(loads)

class Faktur(Master):
	pass