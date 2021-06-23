class Table():

	table = []

	def commit_row(self, row):
		self.table.append(row.data())

	def data(self):
		return self.table
		
	class Row():

		row = []

		def __init__(self):
			pass

		def data(self):
			return self.row

		def set_primary_key(self, primary_key):
			self.row.append({ 
				'type' : "text",
				'text' : primary_key 
			})

		def text(self, text=""):
			self.row.append({ 
				'type' : "text",  
				'text' : text 
			})

		def badge(self, text=""):
			self.row.append({ 
				'type' : "badge",  
				'text' : text
			})

		def badge_danger(self, text=""):
			self.row.append({ 
				'type' : "badge_danger",  
				'text' : text
			})

		def badge_warning(self, text=""):
			self.table_group.append({ 
				'type' : "badge_warning",  
				'text' : text
			})

		def price(self, text=""):
			self.row.append({
				'type' : "price",  
				'text' : text
			})

