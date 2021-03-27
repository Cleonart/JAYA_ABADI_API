from mysql import connExecute

class opt():

	def kategori():
		"""Option for kategori"""
		option_list = connExecute("SELECT * FROM `kategori`")
		option = []
		for option_ in option_list:
			option.append({
				'value' : option_['kategori_id'],
				'label' : option_['kategori_nama'].upper()
			})
		return option

	def merek():
		option_list = connExecute("SELECT * FROM `merek`")
		option = []
		for option_ in option_list:
			option.append({
				'label' : option_['merek_nama'].upper(), 
				'value' : option_['merek_id']
			})
		return option

	def satuan():
		option_list = connExecute("SELECT * FROM `satuan`")
		option = []
		for option_ in option_list:
			option.append({
				'label' : option_['satuan_nama'].upper(), 
				'value' : option_['satuan_id']
			})
		return option