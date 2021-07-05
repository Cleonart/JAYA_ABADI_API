from Mappy.mysql import SQLBuilder

def set_value(label, value):
	return { 'label' : label,'value' : value }

def get_value(table_name):
	return SQLBuilder().select("*", table_name).execute()

class option():

	def kategori():
		""" Option list for kategori """
		option = []
		for option_ in get_value('kategori'):
			option.append(set_value(option_['kategori_nama'].upper(), option_['kategori_id']))
		return option

	def merek():
		""" Option list for merek """
		option = []
		for option_ in get_value('merek'):
			option.append(set_value(option_['merek_nama'].upper(), option_['merek_id']))
		return option

	def satuan():
		""" Option list for satuan """
		option = []
		for option_ in get_value('satuan'):
			option.append(set_value(option_['satuan_nama'].upper(), option_['satuan_id']))
		return option

	def posisi():
		option = []
		for option_ in get_value('posisi'):
			option.append(set_value(option_['posisi_nama'].upper(), option_['posisi_id']))
		return option

	def status():
		option = []
		option.append(set_value("Aktif", 1))
		option.append(set_value("Tidak Aktif", 0))
		return option

	def provinsi():
		option = []
		option.append(set_value("Sulawesi Utara", "Sulawesi Utara"))
		return option
	
	def kota():
		option = []
		option.append(set_value("Manado", "Manado"))
		option.append(set_value("Tomohon", "Tomohon"))
		option.append(set_value("Kotamobagu", "Kotamobagu"))
		option.append(set_value("Airmadidi", "Airmadidi"))
		return option

	def objectDataPosisiStok():
		json_data = {}
		json_data['toko'] = "Toko"
		json_data['gudang'] = "Gudang"
		return json_data

	def objectDataSupplier():
		json_data = {}
		temporary_data = SQLBuilder().select("*", "master_supplier") \
						.where("`supplier_nama` != 'UMUM'") \
						.execute()
		json_data['SUPGENERAL'] = "UMUM"
		for data in temporary_data:
			json_data[data['supplier_id']] = "{}".format(data['supplier_nama'].title())
		return json_data

	def objectDataBarang():
		json_data = {}
		sql = SQLBuilder().select("*", "barang") \
			.inner_join("kategori").on("`barang`.barang_kategori = `kategori`.kategori_id") \
			.inner_join("merek").on("`barang`.barang_merek = `merek`.merek_id") \
			.where(f"barang.barang_status = '1'").execute()
		
		for data in sql:
			json_data[data['barang_id']] = "[{}] {} - {} {}".format(data['kategori_nama'],data['merek_nama'],data['barang_nama'],data['barang_varian'])
		return json_data
	
	def objectDataSatuan():
		json_data = {}
		temporary_data = SQLBuilder().select("*", "satuan").execute()
		for data in temporary_data:
			json_data[data['satuan_id']] = "{}".format(data['satuan_nama'])	
		return json_data

	def objectDataPelanggan():
		json_data = {}
		temporary_data = SQLBuilder().select("*", "master_pelanggan").execute()
		for data in temporary_data:
			json_data[data['pelanggan_id']] = "{}".format(data['pelanggan_nama'])	
		return json_data

	def objectDataPengguna(staffType=None):
		json_data = {}
		sql = SQLBuilder().select("*", "pengguna")
		if staffType :
			sql = sql.where("`pengguna_posisi` = '{}' ".format(staffType))
		temporary_data = sql.execute()

		for data in temporary_data:
			json_data[data['pengguna_id']] = "{}".format(data['pengguna_nama'])	
		return json_data