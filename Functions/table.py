class table():

	table_group = []

	def __init__(self, id):
		self.table_group = []
		self.table_group.append({ 
			'type' : "text",  
			'text' : id 
		})

	def get(self):
		return self.table_group

	def add_field_text(self, text=""):
		self.table_group.append({ 
			'type' : "text",  
			'text' : text 
		})

	def add_field_badge(self, text=""):
		self.table_group.append({ 
			'type' : "badge",  
			'text' : text
		})

	def add_field_badge_danger(self, text=""):
		self.table_group.append({ 
			'type' : "badge_danger",  
			'text' : text
		})

	def add_field_price(self, text=""):
		self.table_group.append({
			'type' : "price",  
			'text' : text
		})